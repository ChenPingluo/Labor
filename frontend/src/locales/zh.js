export default {
  common: {
    login: '登录',
    logout: '退出登录',
    username: '用户名',
    password: '密码',
    submit: '提交',
    cancel: '取消',
    add: '新增',
    save: '保存',
    query: '查询',
    remark: '备注',
    operation: '操作',
    noData: '暂无数据',
    pleaseSelect: '请选择',
    pleaseInput: '请输入',
    success: '操作成功',
    error: '操作失败',
    type: '类型',
    amount: '金额',
    time: '时间',
    id: 'ID',
    warehouse: '仓库',
    item: '商品',
    quantity: '数量',
    optionalRemark: '可选备注',
    saveRecord: '保存记录',
    name: '名称',
    remarkPlaceholder: '说明...'
  },
  menu: {
    dashboard: '仪表盘',
    items: '商品管理',
    warehouses: '仓库管理',
    inventory: '库存流水',
    stock: '库存总览',
    finance: '财务管理'
  },
  login: {
    title: '系统登录',
    usernamePlaceholder: '请输入用户名',
    passwordPlaceholder: '请输入密码',
    loginButton: '登录',
    loginFailed: '登录失败，请检查网络或联系管理员'
  },
  dashboard: {
    title: '仪表盘',
    welcome: '欢迎回来',
    intro: '这里是系统概览。请从左侧菜单选择功能。',
    quickAccess: '快速入口',
    manageItems: '管理商品',
    viewInventory: '查看库存'
  },
  finance: {
    title: '财务管理',
    addRecord: '新增财务记录',
    recordList: '财务记录列表',
    type: {
      rent: '应收',
      pay: '应付',
      collect: '收款',
      payment: '付款'
    },
    rustCalc: '库存价值计算 (Rust引擎)',
    calcButton: '开始计算',
    totalValue: '总价值',
    itemCount: '商品数量',
    engine: '计算引擎'
  },
  inventory: {
    title: '库存流水',
    addRecord: '新增记录',
    recordList: '流水记录',
    selectWarehouse: '请选择仓库',
    selectItem: '请选择商品',
    type: {
      in: '入库',
      out: '出库'
    },
    error: {
      warehouseAndItemRequired: '仓库 和 商品 必须选择',
      quantityMustBePositive: '数量必须大于 0'
    }
  },
  items: {
    title: '商品管理',
    addItem: '新增商品',
    itemList: '商品列表',
    sku: 'SKU',
    skuPlaceholder: '例如: ITEM-001',
    name: '商品名称',
    namePlaceholder: '例如: 螺丝刀',
    unit: '单位',
    unitPlaceholder: 'pcs',
    error: {
      skuAndNameRequired: 'sku 和 名称 必填'
    }
  },
  stock: {
    title: '库存总览',
    filter: '查询筛选',
    result: '库存结果',
    allItems: '全部商品',
    allWarehouses: '全部仓库',
    currentStock: '当前库存'
  },
  warehouses: {
    title: '仓库管理',
    addWarehouse: '新增仓库',
    warehouseList: '仓库列表',
    name: '仓库名称',
    namePlaceholder: '例如: 主仓库',
    location: '位置',
    locationPlaceholder: '例如: A区',
    error: {
      nameRequired: '仓库名称必填'
    }
  }
}
