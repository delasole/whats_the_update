
function OrderHistoryContainer(props) {
    const[OrderHistoryData, setOrderHistoryData] = React.useState(null);

    React.useEffect(() => {
        fetch('/api/orders.json').
        then((response) => response.json()).
        then((data) => {setOrderHistoryData(data.orders);})
    })
}