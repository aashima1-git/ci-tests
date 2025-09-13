# ci-tests
Sanity and regression testing with CI/CD jenkins

# CI Automated Sanity & Regression Testing

## 🔹 Purpose
Automate sanity and regression testing in Jenkins CI/CD pipeline.

## 🔹 Setup

### 1. Clone repo
```bash
git clone https://github.com/your-username/ci-tests.git
cd ci-tests
```

### 2. Install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run tests locally
```bash
pytest tests/test_sanity.py --html=reports/sanity.html --self-contained-html
pytest tests/test_regression.py --html=reports/regression.html --self-contained-html
```

### 4. Jenkins Setup
- Install plugins: **Pipeline, Git, HTML Publisher**
- Create pipeline job → Link GitHub repo
- Add `Jenkinsfile`
- Run build → Check **Test Reports** in Jenkins

## 🔹 Output
- Automated test execution in CI
- HTML reports in Jenkins
- Faster feedback on build health

