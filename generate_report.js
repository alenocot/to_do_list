var reporter = require('cucumber-html-reporter');

var options = {
    theme: 'bootstrap',
    jsonFile: 'cucumber_report_fixed.json', // Use the fixed JSON file
    output: 'cucumber_report.html',
    reportSuiteAsScenarios: true,
    launchReport: true,
    name: 'Alejandra Cotrina',
    brandTitle: 'To-Do List Management Test Report'
};

reporter.generate(options);

console.log('HTML report generated as cucumber_report.html');
