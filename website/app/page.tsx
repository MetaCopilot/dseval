'use client';

import { useEffect, useState } from 'react';
import { styled } from '@mui/material/styles';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import Divider from '@mui/material/Divider';

import { SimpleTreeView } from '@mui/x-tree-view/SimpleTreeView';
import { TreeItem } from '@mui/x-tree-view/TreeItem';


const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));


export default function Home() {

  const [benchmarks, setBenchmarks] = useState({});
  const [results, setResults] = useState([]);

  useEffect(() => {
    Promise.all([
      fetch('/data/benchmarks.json'),
      fetch('/data/results.json')
    ]).then(([res1, res2]) => {
      return Promise.all([res1.json(), res2.json()]);
    }).then(([benchmarkData, resultsData]) => {
      setBenchmarks(benchmarkData);
      setResults(resultsData);
    });
  });

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="sticky">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            DSEval Online Browser
          </Typography>
        </Toolbar>
      </AppBar>

      <Grid container spacing={2}>
        <Grid item xs={5}>
        <SimpleTreeView
          sx={{ height: 200, flexGrow: 1, maxWidth: 400, overflowY: 'auto' }}
        >
          {
            Object.entries(benchmarks).map(([benchmarkName, benchmarkContents], index) => (
              <TreeItem itemId={`benchmark-${index}`} label={benchmarkName}>
                {
                  benchmarkContents.map((content) => content.problemset)
                  .sort().filter((item, pos, array) => !pos || item != array[pos - 1])
                  .map((problemsetName, localIndex) => (
                    <TreeItem itemId={`benchmark-${index}-${localIndex}`} label={problemsetName} />
                  ))
                }
              </TreeItem>
            ))
          }
        </SimpleTreeView>
        </Grid>
        <Grid item xs={7}>
          <Item>xs=4</Item>
        </Grid>
      </Grid>

    </Box>
  );
}
