export default {
  common: {
    login: 'Login',
    logout: 'Logout',
    username: 'Username',
    password: 'Password',
    submit: 'Submit',
    cancel: 'Cancel',
    add: 'Add',
    save: 'Save',
    query: 'Query',
    remark: 'Remark',
    operation: 'Operation',
    noData: 'No Data',
    pleaseSelect: 'Please Select',
    pleaseInput: 'Please Input',
    success: 'Success',
    error: 'Error',
    type: 'Type',
    amount: 'Amount',
    time: 'Time',
    id: 'ID',
    warehouse: 'Warehouse',
    item: 'Item',
    quantity: 'Quantity',
    optionalRemark: 'Optional remark',
    saveRecord: 'Save Record',
    name: 'Name',
    remarkPlaceholder: 'Description...'
  },
  menu: {
    dashboard: 'Dashboard',
    items: 'Item Management',
    warehouses: 'Warehouse Management',
    inventory: 'Inventory Log',
    stock: 'Stock Overview',
    finance: 'Finance Management'
  },
  login: {
    title: 'System Login',
    usernamePlaceholder: 'Enter username',
    passwordPlaceholder: 'Enter password',
    loginButton: 'Login',
    loginFailed: 'Login failed, please check network or contact admin'
  },
  dashboard: {
    title: 'Dashboard',
    welcome: 'Welcome Back',
    intro: 'System overview. Please select a function from the left menu.',
    quickAccess: 'Quick Access',
    manageItems: 'Manage Items',
    viewInventory: 'View Inventory'
  },
  finance: {
    title: 'Finance Management',
    addRecord: 'Add Finance Record',
    recordList: 'Finance Record List',
    type: {
      rent: 'Receivable',
      pay: 'Payable',
      collect: 'Collection',
      payment: 'Payment'
    },
    rustCalc: 'Inventory Value Calculation (Rust Engine)',
    calcButton: 'Calculate',
    totalValue: 'Total Value',
    itemCount: 'Item Count',
    engine: 'Engine'
  },
  inventory: {
    title: 'Inventory Log',
    addRecord: 'Add Record',
    recordList: 'Log Records',
    selectWarehouse: 'Select Warehouse',
    selectItem: 'Select Item',
    type: {
      in: 'Inbound',
      out: 'Outbound'
    },
    error: {
      warehouseAndItemRequired: 'Warehouse and Item are required',
      quantityMustBePositive: 'Quantity must be greater than 0'
    }
  },
  items: {
    title: 'Item Management',
    addItem: 'Add Item',
    itemList: 'Item List',
    sku: 'SKU',
    skuPlaceholder: 'e.g. ITEM-001',
    name: 'Item Name',
    namePlaceholder: 'e.g. Screwdriver',
    unit: 'Unit',
    unitPlaceholder: 'pcs',
    error: {
      skuAndNameRequired: 'SKU and Name are required'
    }
  },
  stock: {
    title: 'Stock Overview',
    filter: 'Filter',
    result: 'Stock Result',
    allItems: 'All Items',
    allWarehouses: 'All Warehouses',
    currentStock: 'Current Stock'
  },
  warehouses: {
    title: 'Warehouse Management',
    addWarehouse: 'Add Warehouse',
    warehouseList: 'Warehouse List',
    name: 'Warehouse Name',
    namePlaceholder: 'e.g. Main Warehouse',
    location: 'Location',
    locationPlaceholder: 'e.g. Zone A',
    error: {
      nameRequired: 'Warehouse name is required'
    }
  }
}
