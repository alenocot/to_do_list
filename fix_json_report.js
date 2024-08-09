const fs = require('fs');

const jsonData = JSON.parse(fs.readFileSync('cucumber_report.json', 'utf8'));

// Ensure each feature has a 'uri' field
jsonData.forEach(feature => {
  if (!feature.uri) {
    feature.uri = feature.location.split(':')[0];
  }
});

// Save the modified JSON report
fs.writeFileSync('cucumber_report_fixed.json', JSON.stringify(jsonData, null, 2));

console.log('Fixed JSON report generated as cucumber_report_fixed.json');
