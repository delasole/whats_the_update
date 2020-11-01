
function OrderHistory(props) {
    return (
        <div onClick={() => href='/messagecenter/${props.order_id}'}className='order-history'>
            <p>{props.phone}</p>
            <p>{props.firstname}</p>
            <p>{props.lastname}</p>
            <p>{props.orderdate}</p>
            <p>{props.item}</p>
        </div>
    )
}

function OrderHistoryContainer(props) {
    const[OrderHistoryData, setOrderHistoryData] = React.useState(null);

    React.useEffect(() => {
        fetch('/api/orders.json').
        then((response) => response.json()).
        then((data) => {setOrderHistoryData(data.orders);})
        console.log('here')
    }, [])

const orderHistories = [];
for(const orderHistory of OrderHistoryData){
    orderHistories.push(
        <OrderHistory
        order_id={orderHistory.order_id}
        firstname = {orderHistory.first_name}
        lastname = {orderHistory.last_name}
        phone = {orderHistory.phone}
        item = {orderHistory.item}
        orderdate = {orderHistory.order_date}/>
    );
}

return(
    <React.Fragment>
        {orderHistories}
    </React.Fragment>
    )
}
ReactDOM.render(<OrderHistoryContainer orderHistories={OrderHistoryData}/>,
    document.getElementById('order-history'));