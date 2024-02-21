### Dataset name ###

Vietnamese Job Posting - Vietnamese Version

### Dataset description ###

The dataset contains approximately 2,000 job postings from the CareerBuilder job posting platform. The Scrapy library was used to extract the data from this website. This was the Vietnamese Job Posting data in early 2023.

A job posting typically has some structure, though some fields of the posting may not. The data was unprocessed.

## **Content**

job_title - The original job title.
job_id - The unique ID of the corresponding job.
job_url - The link of the job.
company_title - Name of the company.
company_url - The official website of the company.
company_video_url - The official video link of the company.
salary - The salary of the job.
location - Location of the working place.
outstanding_welfare - Outstanding welfare of the corresponding position.
annoucement_date - Job posting announcement date.
category - The specific type of the job.
position - Position in the company.
exp - Required experience years for the position.
order - Rank of the position.
expiration_date - Job posting expiration date.
detailed_welfare - Full welfare.
job_description - Job description.
job_requirements - Job requirements.
other_info - Other information of the job.
job_tags - Highlight tags of the job.

### Dataset files ###

- vietnamese-job-posting.csv

    pandas.DataFrame(shape=(2056, 20), columns=["job_title", "job_id", "job_url", "company_title", "company_url", "company_video_url", "salary", "location", "outstanding_welfare", "announcement_date", "category", "position", "exp", "order", "expiration_date", "detailed_welfare", "job_description", "job_requirements", "other_info", "job_tags"])
                        job_title    job_id              job_url        company_title          company_url    company_video_url               salary  ...                order expiration_date     detailed_welfare      job_description     job_requirements           other_info             job_tags
        0     Performance Mark...  35BB6CB4  https://careerbu...  Công ty Cổ phần ...  https://careerbu...  https://www.yout...  Lương: 15 Tr - 2...  ...            Nhân viên      31/03/2023  Laptop | Chế độ ...  <div class="deta...  <div class="deta...  <div class="deta...                  NaN
        1     Organization Dev...  35BB6E66  https://careerbu...  Công ty Cổ phần ...  https://careerbu...  https://www.yout...  Lương: 30 Tr - 4...  ...  Trưởng nhóm / Gi...      31/03/2023  Laptop | Chế độ ...  <div class="deta...  <div class="deta...  <div class="deta...   Purchasing |  N...
        2     Thiết kế đồ họa-...  35BB6CF1  https://careerbu...  Công Ty TNHH TM ...  https://careerbu...                  NaN  Lương: 12 Tr - 2...  ...            Nhân viên       10/3/2023  Chế độ bảo hiểm ...  <div class="deta...  <div class="deta...  <div class="deta...   Họa viên |  UI ...
        3     [HCM-Phú Nhuận] ...  35BB6E1A  https://careerbu...              Bảo mật  javascript:void(0);                  NaN  Lương: 10 Tr - 1...  ...            Nhân viên      13/03/2023  Laptop | Chế độ ...  <div class="deta...  <div class="deta...  <div class="deta...   Sales Executive...
        4     Nhân Viên Kinh D...  35BB6CBF  https://careerbu...  Công Ty TNHH TM ...  https://careerbu...                  NaN    Lương: Cạnh tranh  ...            Nhân viên       10/3/2023  Chế độ bảo hiểm ...  <div class="deta...  <div class="deta...  <div class="deta...   Đại diện kinh d...
        ...                   ...       ...                  ...                  ...                  ...                  ...                  ...  ...                  ...             ...                  ...                  ...                  ...                  ...                  ...
        2051  84603 - Sales Ou...  35BB3E35  https://careerbu...  RGF HR Agent Vie...  https://careerbu...                  NaN  Lương: 15 Tr - 3...  ...            Nhân viên      18/03/2023  Chế độ bảo hiểm ...  <div class="deta...  <div class="deta...  <div class="deta...  - Sales Outdoor ...
        2052  Nhân Viên Phòng ...  35BB3E2F  https://careerbu...  Công Ty TNHH Har...  https://careerbu...                  NaN    Lương: Cạnh tranh  ...            Nhân viên      18/03/2023  Chế độ bảo hiểm ...  <div class="deta...  <div class="deta...  <div class="deta...   Production Tech...
        2053  CHUYÊN VIÊN VẬN ...  35BB3DD5  https://careerbu...  Công ty TNHH Tru...  https://careerbu...                  NaN  Lương: 12 Tr - 1...  ...            Nhân viên      18/03/2023  Chế độ bảo hiểm ...  <div class="deta...  <div class="deta...  <div class="deta...  TMĐT |  Tech & P...
        2054  Kiểm soát viên -...  35BB3E33  https://careerbu...  Ngân hàng Thương...  https://careerbu...  https://www.yout...    Lương: Cạnh tranh  ...  Trưởng nhóm / Gi...      18/03/2023  Chế độ bảo hiểm ...  <div class="deta...  <div class="deta...  <div class="deta...  Kiểm soát viên -...
        2055  Đại Diện Tiêu Th...  35BB3D97  https://careerbu...    HEINEKEN Vietnam   https://careerbu...  https://www.yout...    Lương: Cạnh tranh  ...                  NaN             NaN                  NaN  <div class="deta...  <div class="deta...  <div class="deta...  Đại Diện Tiêu Th...

