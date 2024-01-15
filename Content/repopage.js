  function generateTableRows(data) {
    const tbody = $('#clickableTable tbody');
    tbody.empty(); // Clear existing rows
    
    data.forEach(item => {
      const row = `<tr id="${item.hash}" onclick="handleRowClick('${item.hash}')">
                    <td>${item.name}</td>
                    <td>${item.arch}</td>
                    <td>${item.version}</td>
                    <td>${item.hash}</td>
                  </tr>`;
      tbody.append(row);
    });
  }

  function generateDetailsRows(data) {
    const tbody = $('#packageDetails tbody');
    tbody.empty(); // Clear existing rows
    
    Object.entries(data).forEach(([key, value]) => {
      const row = `<tr id="desc_${key}">
                    <td>${key}</td>
                    <td>${value}</td>
                  </tr>`;
      tbody.append(row);
    });
  }

  function handlenavClick(repo_name) {
    $.getJSON('/api/Package?action=list&repo_name='+repo_name, function(data) {
      generateTableRows(data);
    });
  }

  function handleRowClick(id) {
    var baseItem= $("#"+id)[0]
    var itemArch = baseItem.childNodes[0].innerText
    var itemName = baseItem.childNodes[1].innerText
    var itemVersion = baseItem.childNodes[2].innerText
    var itemHash = baseItem.childNodes[3].innerText
    var dataString="package_name="+itemArch+"&arch="+itemName+"&version="+itemVersion+"&hash="+itemHash

    $.getJSON('/api/Package?action=get&'+dataString, function(data) {
      generateDetailsRows(data);
    });
  }

