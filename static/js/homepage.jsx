function Order(props) {
  const {order} = props;
  return (
    <div onClick='/messagecenter/`${order.order_id}`'>
      <p>{order.order_id}</p>
      <p>{order.order_date}</p>
      <p>{order.first_name} {order.last_name}</p>
      <p>{order.phone}</p>
      <p>{order.item}</p>
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