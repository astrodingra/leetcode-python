# LeetCode Solutions in Python

Welcome to my repository where I upload solutions to LeetCode problems that I have solved in Python. I will be updating this repository with new solutions as I complete more problems.

## Solutions

| Problem Number | Problem Name      | Solution Link                   | Difficulity |
|----------------|-------------------|---------------------------------|-------------|
| 1              | Two Sum           | [Solution](two_sum.py) |Easy|
| 9              | Palindrome Number | [Solution](palindrome_number.py) |Easy|
<!-- Add more rows as you solve more problems -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeetCode Progress</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        .container {
            width: 300px;
            margin: auto;
        }
        canvas {
            max-width: 100%;
        }
        .progress-info {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 18px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>LeetCode Progress</h1>
        <div style="position: relative;">
            <canvas id="progressChart" width="300" height="300"></canvas>
            <div class="progress-info" id="progressInfo">0/0</div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        // Initialize Chart.js
        const ctx = document.getElementById('progressChart').getContext('2d');
        const progressInfoElement = document.getElementById('progressInfo');

        // Function to update chart and problem count
        function updateProgress(easySolved, mediumSolved, hardSolved, totalEasy, totalMedium, totalHard) {
            const totalSolved = easySolved + mediumSolved + hardSolved;
            const totalProblems = totalEasy + totalMedium + totalHard;
            const easyPercentage = (easySolved / totalProblems) * 100;
            const mediumPercentage = (mediumSolved / totalProblems) * 100;
            const hardPercentage = (hardSolved / totalProblems) * 100;
            const remainingPercentage = 100 - (easyPercentage + mediumPercentage + hardPercentage);
            
            progressInfoElement.textContent = `${totalSolved}/${totalProblems}`;

            const chart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Easy', 'Medium', 'Hard', 'Remaining'],
                    datasets: [{
                        data: [easyPercentage, mediumPercentage, hardPercentage, remainingPercentage],
                        backgroundColor: ['#4caf50', '#ffa726', '#f44336', '#e0e0e0'],
                        borderWidth: 0,
                        borderRadius: 5, // Make the bar edges rounded
                        weight: 2
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        },
                        tooltip: {
                            enabled: false
                        },
                    },
                    cutout: '80%', // Adjust the cutout for thinner bar
                }
            });
        }

        // Example usage
        const totalEasy = 811;
        const totalMedium = 1692;
        const totalHard = 718;
        const easySolved = 200; // Update this value to reflect the number of easy problems solved
        const mediumSolved = 300; // Update this value to reflect the number of medium problems solved
        const hardSolved = 100; // Update this value to reflect the number of hard problems solved
        updateProgress(easySolved, mediumSolved, hardSolved, totalEasy, totalMedium, totalHard);
    </script>
</body>
</html>

## How to Use

1. Clone the repository:
   ```sh
   git clone https://github.com/astrodingra/leetcode-python.git
