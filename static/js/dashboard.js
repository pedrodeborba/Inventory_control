$(function () {
  $.ajax({
    url: "/dashboard/chart-data/",
    method: "GET",
    success: function (response) {
      // Gráfico de ordens
      var chartData = {
        series: [
          {
            name: "Total de Ordens",
            type: "bar",
            data: response.order_chart.totals
          },
          {
            name: "Ordens por Filial",
            type: "bar",
            data: response.orders_by_branch.data
          }
        ],
        chart: {
          type: "bar",
          height: 345,
          offsetX: -15,
          toolbar: { show: true },
          foreColor: "#adb0bb",
          fontFamily: 'inherit',
          sparkline: { enabled: false },
        },
        colors: ["#5D87FF", "#49BEFF"],
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: "25%",
            borderRadius: [6],
            borderRadiusApplication: 'end',
            borderRadiusWhenStacked: 'all'
          },
        },
        markers: { size: 0 },
        dataLabels: { enabled: false },
        legend: {
          show: true,
          position: "top",
          horizontalAlign: "center"
        },
        grid: {
          borderColor: "rgba(0,0,0,0.1)",
          strokeDashArray: 3,
          xaxis: {
            lines: { show: false },
          },
        },
        xaxis: {
          type: "category",
          categories: response.order_chart.dates,
          labels: {
            style: { cssClass: "grey--text lighten-2--text fill-color" },
          },
        },
        yaxis: [
          {
            title: { text: "Total de Ordens" },
            min: 0,
            labels: {
              style: { cssClass: "grey--text lighten-2--text fill-color" },
            },
          },
          {
            opposite: true,
            title: { text: "Ordens por Filial" },
            min: 0,
            labels: {
              style: { cssClass: "grey--text lighten-2--text fill-color" },
            },
          }
        ],
        stroke: {
          show: true,
          width: 3,
          lineCap: "butt",
          colors: ["transparent"],
        },
        tooltip: { theme: "light" },
        responsive: [
          {
            breakpoint: 600,
            options: {
              plotOptions: { bar: { borderRadius: 3 } },
            }
          }
        ]
      };
      new ApexCharts(document.querySelector("#chart"), chartData).render();

      // =====================================
      // Funcionários
      // =====================================
      var staff = {
        series: response.staff_chart_data.data,
        labels: response.staff_chart_data.labels,
        chart: {
          width: 180,
          type: "donut",
          fontFamily: "Plus Jakarta Sans', sans-serif",
          foreColor: "#adb0bb",
        },
        plotOptions: {
          pie: {
            startAngle: 0,
            endAngle: 360,
            donut: { size: '75%' },
          },
        },
        stroke: { show: false },
        dataLabels: { enabled: true },
        legend: { show: false },
        colors: ["#5D87FF", "#FF6F61", "#FF8C00", "#32CD32", "#6A5ACD"],
        responsive: [
          {
            breakpoint: 991,
            options: {
              chart: { width: 300 },
            },
          },
        ],
        tooltip: { theme: "dark", fillSeriesColor: false },
      };
      new ApexCharts(document.querySelector("#staff"), staff).render();

      // =====================================
      // Empréstimo
      // =====================================

      // Total de empréstimos
      const totalLoans = response.loan_chart.loan_totals.reduce((a, b) => a + b, 0);
      document.getElementById('total-loans').textContent = totalLoans;

      // Percentual de crescimento do último mês
      const totalLoansThisMonth = response.loan_chart.loan_totals.slice(-1)[0] || 0;
      const totalLoansLastMonth = response.loan_chart.loan_totals.slice(-2, -1)[0] || 0;
      let growthPercentage = totalLoansLastMonth > 0
        ? ((totalLoansThisMonth - totalLoansLastMonth) / totalLoansLastMonth) * 100
        : 0;

      // Adiciona o sinal de "+" ou "-" dependendo do valor do crescimento
      let growthSign = growthPercentage > 0 ? '+' : growthPercentage < 0 ? '-' : '';
      growthPercentage = Math.abs(growthPercentage);  // Remove o sinal negativo para formatar corretamente

      // Exibe o valor formatado no HTML
      document.getElementById('growth-percentage').textContent = `${growthSign}${growthPercentage.toFixed(2)}% Último mês`;

      const loanTotals = response.loan_chart.loan_totals.map(total => Math.round(total));

      // Configuração do gráfico
      var loan = {
        chart: {
          id: "sparkline3",
          type: "area",
          height: 60,
          sparkline: { enabled: true },
          group: "sparklines",
          fontFamily: "Plus Jakarta Sans', sans-serif",
          foreColor: "#adb0bb",
        },
        series: [
          {
            name: "Empréstimos",
            color: "#49BEFF",
            data: loanTotals,  // Usando os totais de empréstimos
          },
        ],
        stroke: { curve: "smooth", width: 2 },
        fill: { colors: ["#f3feff"], type: "solid", opacity: 0.05 },
        markers: { size: 0 },
        tooltip: {
          theme: "dark",
          fixed: { enabled: true, position: "right" },
          x: { show: true },
        },
        xaxis: {
          categories: response.loan_chart.loan_dates,  // Usando as datas de retirada
          labels: {
            style: { cssClass: "grey--text lighten-2--text fill-color" },
            format: 'dd/MM/yyyy'
          },
        }
      };

      new ApexCharts(document.querySelector("#loan-chart"), loan).render();
    },
    error: function (error) {
      console.error("Erro ao buscar dados do gráfico:", error);
    }
  });
});
