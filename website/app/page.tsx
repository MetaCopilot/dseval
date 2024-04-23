"use client";

import React, { useEffect, useState } from "react";
import { styled } from "@mui/material/styles";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Drawer from '@mui/material/Drawer';
import Toolbar from "@mui/material/Toolbar";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import Divider from "@mui/material/Divider";
import Modal from "@mui/material/Modal";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";

import { SimpleTreeView } from "@mui/x-tree-view/SimpleTreeView";
import { TreeItem } from "@mui/x-tree-view/TreeItem";

interface ProblemSet {
  name: string;
  problemCount: number;
  averageDifficulty: number;
}

interface Problem {
  benchmark: string;
  problemset: string;
  index: number;
  setup: string;
  code: string;
  difficulty: number;
}

interface Result {
  benchmark: string;
  version: number;
  problemset: string;
  index: number;
  agent: string;
  attempt: number;
  verdict: string;
  subverdict: string;
  extended_verdict: string;
  question: string;
  agent_exception: string;
  validator: any[];
}

interface SiteData {
  // Benchmark name to a list of problemsets
  benchmarks: Map<string, ProblemSet[]>;
  // Benchmark name, problemset to a list of problems
  problems: Map<string, Problem[]>;
  // From benchmark, problemset, index to a list of results
  results: Map<string, Result[]>;
}

function ResultDrawer() {
  return <div/>;
}

export default function Home() {
  const [data, setData] = useState<SiteData>({
    benchmarks: new Map(),
    problems: new Map(),
    results: new Map(),
  });
  const [visibleProblems, setVisibleProblems] = useState<Problem[]>([]);
  const [resultSet, setResultSet] = useState<Result[] | undefined>(undefined);

  const SEPARATOR = "---";

  useEffect(() => {
    Promise.all([fetch("/data/benchmarks.json"), fetch("/data/results.json")])
      .then(([res1, res2]) => {
        return Promise.all([res1.json(), res2.json()]);
      })
      .then(([benchmarkData, resultsData]) => {
        const problems = new Map<string, Problem[]>();
        Object.entries(benchmarkData).forEach(([benchmarkName, problemsets]) => {
          (problemsets as Problem[]).forEach((problem) => {
            problems.set(`${benchmarkName}${SEPARATOR}${problem.problemset}`, [
              ...(problems.get(`${benchmarkName}${SEPARATOR}${problem.problemset}`) || []),
              problem,
            ]);
          });
        });

        const benchmarks = new Map<string, ProblemSet[]>();
        Array.from(problems.entries()).forEach(([benchmarkNameAndName, problemList]) => {
          const [benchmarkName, name] = benchmarkNameAndName.split(SEPARATOR);
          const problemCount = problemList.filter((problem) => problem.setup.length > 0).length;
          const averageDifficulty =
            problemList
              .filter((problem) => problem.setup.length > 0)
              .reduce((acc, problem) => acc + problem.difficulty, 0) / problemCount;
          benchmarks.set(benchmarkName, [
            ...(benchmarks.get(benchmarkName) || []),
            {
              name,
              problemCount,
              averageDifficulty,
            },
          ]);
        });

        const results = new Map<string, Result[]>();
        Object.entries(resultsData).forEach(([benchmarkName, resultData]) => {
          (resultData as Result[]).forEach((result) => {
            results.set(
              `${result.benchmark}${SEPARATOR}${result.problemset}${SEPARATOR}${result.index}`,
              [
                ...(results.get(
                  `${result.benchmark}${SEPARATOR}${result.problemset}${SEPARATOR}${result.index}`
                ) || []),
                result,
              ]
            );
          });
        });

        setData({
          benchmarks,
          problems,
          results,
        });
      });
  }, []);

  const handleProblemSetClick =
    (benchmark: string, problemset: string) => (event: React.MouseEvent) => {
      const problems = data.problems.get(`${benchmark}${SEPARATOR}${problemset}`)!;
      setVisibleProblems(problems);
    };

  const drawer = (
    <Drawer open={resultSet !== undefined} onClose={() => setResultSet(undefined)}>
    </Drawer>
  )

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="fixed">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            DSEval Online Browser
          </Typography>
        </Toolbar>
      </AppBar>

      <Grid container spacing={2} sx={{ marginTop: "80px" }}>
        <Grid item xs={5} sx={{ maxHeight: "calc(100vh - 80px)", overflow: "auto" }}>
          <SimpleTreeView>
            {Array.from(data.benchmarks.entries()).map(
              ([benchmarkName, benchmarkContents], index) => {
                const numProblemsets = benchmarkContents.length;
                const numProblems = benchmarkContents.reduce(
                  (acc, problemset) => acc + problemset.problemCount,
                  0
                );
                const averageDifficulty =
                  benchmarkContents.reduce(
                    (acc, problemset) =>
                      acc + problemset.averageDifficulty * problemset.problemCount,
                    0
                  ) / numProblems;
                return (
                  <TreeItem
                    itemId={`benchmark-${index}`}
                    label={`${benchmarkName} (${numProblemsets} problemsets, ${numProblems} problems, difficulty ${averageDifficulty.toFixed(
                      1
                    )})`}
                  >
                    {benchmarkContents.map((problemset, localIndex) => (
                      <TreeItem
                        itemId={`benchmark-${index}-${localIndex}`}
                        label={`${problemset.name} (${
                          problemset.problemCount
                        } problems, difficulty ${problemset.averageDifficulty.toFixed(1)})`}
                        onClick={handleProblemSetClick(benchmarkName, problemset.name)}
                      />
                    ))}
                  </TreeItem>
                );
              }
            )}
          </SimpleTreeView>
        </Grid>
        <Grid item xs={7} sx={{ maxHeight: "calc(100vh - 80px)", overflow: "auto" }}>
          <Typography variant="h4">
            ProblemSet:{" "}
            {visibleProblems.length > 0 ? visibleProblems[0].problemset : "not selected"}
          </Typography>
          {visibleProblems.map((problem) => {
            const results =
              data.results.get(
                `${problem.benchmark}${SEPARATOR}${problem.problemset}${SEPARATOR}${problem.index}`
              ) || [];
            const acceptRate =
              results.length > 0
                ? (results.filter((result) => result.verdict === "CORRECT").length /
                    results.length) *
                  100
                : 0;

            return (
              <React.Fragment>
                <Typography variant="h6" component="div">
                  {problem.setup
                    ? `Problem #${problem.index} (difficulty ${problem.difficulty.toFixed(
                        1
                      )}, accept rate: ${acceptRate.toFixed(1)}%)`
                    : `Preparation Code #${problem.index}`}
                </Typography>

                {problem.setup ? (
                  <SyntaxHighlighter language="yaml" wrapLongLines={true}>
                    {problem.setup}
                  </SyntaxHighlighter>
                ) : null}
                <SyntaxHighlighter language="python" wrapLongLines={true}>
                  {problem.code}
                </SyntaxHighlighter>
                <Divider />
              </React.Fragment>
            );
          })}
        </Grid>
      </Grid>

      {drawer}

    </Box>
  );
}
