alert("JS Called");

const filterValue = () => {
  storeIdSearc = document.getElementById("StoreId").value;
  skuSearch = document.getElementById("SKU").value;
  productNameSearch = document.getElementById("Product Name").value;
  priceSearch = document.getElementById("Price").value;
  dateSearch = document.getElementById("Date").value;
  $.ajax({
    type: "GET",
    url: "/filterData/1",
    data: {
      storeIdSearc: storeIdSearc,
      skuSearch: skuSearch,
      productNameSearch: productNameSearch,
      priceSearch: priceSearch,
      dateSearch: dateSearch,
    },
    success: function (data) {
      window.location.replace(
        "http://" + window.location.host + "/filterData/0"
      );
    },
  });
};

function highlightEdit(elem) {
  $(elem).css("background", "#e3e3e3");
}

function saveEditedValue(id) {
  editedsku = document.getElementById("sku-" + id);
  editedpNm = document.getElementById("pnm-" + id);
  editedprice = document.getElementById("price-" + id);
  editeddate = document.getElementById("date-" + id);

  if (
    editedsku.getAttribute("data-old_value") === editedsku.innerHTML &&
    editedpNm.getAttribute("data-old_value") === editedpNm.innerHTML &&
    editedprice.getAttribute("data-old_value") === editedprice.innerHTML &&
    editeddate.getAttribute("data-old_value") === editeddate.innerHTML
  )
    return false;

  $.ajax({
    url: "/saveStoreData/" + id,
    type: "get",
    dataType: "json",
    data: {
      sku: editedsku.innerHTML,
      productName: editedpNm.innerHTML,
      price: editedprice.innerHTML,
      date: editeddate.innerHTML,
    },
    success: function (res) {
      if (res) {
        editedsku.style.background = "#FDFDFD";
        editedpNm.style.background = "#FDFDFD";
        editedprice.style.background = "#FDFDFD";
        editeddate.style.background = "#FDFDFD";
      }
    },
    error: function () {
      console.log("errr");
      alert("An error occurred");
    },
  });
}

function reload(e) {
  window.location.replace("http://" + window.location.host + "/");
}
