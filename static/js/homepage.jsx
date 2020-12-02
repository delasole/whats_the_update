function Order(props) {
  const {order} = props;
  return (
        <tr>
          <td className="px-4 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
          <a className="text-blue-500" href={"/messagecenter/" + order.order_id}>{order.order_id}</a>
          </td>
          <td className="px-4 py-4 whitespace-nowrap text-sm text-gray-500">{order.order_date}</td>
          <td className="px-4 py-4 whitespace-nowrap text-sm text-gray-500">{order.first_name} {order.last_name}</td>
          <td className="px-4 py-4 whitespace-nowrap text-sm text-gray-500">{order.item}</td>
        </tr>
  );
}

function OrderHistory() {
  const [orders, setOrders]= React.useState([]);
  React.useEffect(() => {
    fetch('/api/orders.json').
    then((response) => response.json()).
    then((orders)=> setOrders(orders.orders));
  }, []);

  if(orders.length === 0) return <p>You have no orders in the system.</p>
  
  const content = []

  for(const order of orders){
    content.push(<Order key ={order.order_id} order={order}/>);
  }
  return (
    <table className="min-w-lg divide-y divide-gray-200">
    <thead>
      <tr>
        <td scope="col" className="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Order Id</td>
        <td scope="col" className="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Order Date</td>
        <td scope="col" className="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Buyer's Name</td>
        <td scope="col" className="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Item Purchased</td>
      </tr>
    </thead>
    <tbody className="bg-white divide-y divide-gray-200">
    {content}
  </tbody>
  </table>
    );
}

ReactDOM.render(<OrderHistory/>,
  document.getElementById('order-container'));