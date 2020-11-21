function Order(props) {
  const {order} = props;
  return (
    <div>
      <span>Order #</span>
        <td>
          <a href={"/messagecenter/" + order.order_id}>{order.order_id}</a>
        </td>
        <td>{order.order_date}</td>
        <td>{order.first_name} {order.last_name}</td>
        <td>{order.item}</td>
    </div>
  );
}

function OrderHistory() {
  const [orders, setOrders]= React.useState([]);
  React.useEffect(() => {
    fetch('/api/orders.json').
    then((response) => response.json()).
    then((orders)=> setOrders(orders.orders));
  }, []);

  if(orders.length === 0) return <div>Loading...</div>
  
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