function Order(props) {
  const {order} = props;
  return (
  <table className="order-body">
      <thead>
        <tr>
          <td className="order-header">Order Id</td>
          <td className="order-header">Order Date</td>
          <td className="order-header">Buyer's Name</td>
          <td className="order-header">Item Purchase</td>
          <td className="order-header">Last Contacted</td>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td className="order-detail">
            <a href={"/messagecenter/" + order.order_id}>{order.order_id}</a>
          </td>
          <td className="order-detail">{order.order_date}</td>
          <td className="order-detail">{order.first_name} {order.last_name}</td>
          <td className="order-detail">{order.item}</td>
        </tr>
      </tbody>
  </table>  
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
  <div>
    {content}
  </div>
    );
}

ReactDOM.render(<OrderHistory/>,
  document.getElementById('order-container'));