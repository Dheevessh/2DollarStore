import React from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Container,
  Typography,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  IconButton,
  Button,
  Box,
  Divider,
  Alert,
} from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';
import RemoveIcon from '@mui/icons-material/Remove';
import { useCart } from '../contexts/CartContext';

function Cart() {
  const navigate = useNavigate();
  const { cart, removeFromCart, updateQuantity, getTotalPrice, clearCart } = useCart();

  const handleQuantityChange = (productId, currentQuantity, change) => {
    const newQuantity = currentQuantity + change;
    if (newQuantity > 0) {
      updateQuantity(productId, newQuantity);
    } else {
      removeFromCart(productId);
    }
  };

  if (cart.length === 0) {
    return (
      <Container sx={{ mt: 4 }}>
        <Alert severity="info">Your cart is empty</Alert>
        <Button
          variant="contained"
          color="primary"
          onClick={() => navigate('/')}
          sx={{ mt: 2 }}
        >
          Continue Shopping
        </Button>
      </Container>
    );
  }

  return (
    <Container sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>
        Shopping Cart
      </Typography>
      <Alert severity="info" sx={{ mb: 2 }}>
        Shipping fees apply. Estimated delivery time: 2-4 weeks.
      </Alert>
      <List>
        {cart.map((item) => (
          <React.Fragment key={item.id}>
            <ListItem>
              <Box sx={{ display: 'flex', alignItems: 'center', width: '100%' }}>
                <img
                  src={item.image_url}
                  alt={item.title}
                  style={{ width: 80, height: 80, objectFit: 'cover', marginRight: 16 }}
                />
                <ListItemText
                  primary={item.title}
                  secondary={`$${item.price.toFixed(2)} each`}
                />
                <Box sx={{ display: 'flex', alignItems: 'center', mr: 2 }}>
                  <IconButton
                    size="small"
                    onClick={() => handleQuantityChange(item.id, item.quantity, -1)}
                  >
                    <RemoveIcon />
                  </IconButton>
                  <Typography sx={{ mx: 2 }}>{item.quantity}</Typography>
                  <IconButton
                    size="small"
                    onClick={() => handleQuantityChange(item.id, item.quantity, 1)}
                  >
                    <AddIcon />
                  </IconButton>
                </Box>
                <ListItemSecondaryAction>
                  <IconButton
                    edge="end"
                    aria-label="delete"
                    onClick={() => removeFromCart(item.id)}
                  >
                    <DeleteIcon />
                  </IconButton>
                </ListItemSecondaryAction>
              </Box>
            </ListItem>
            <Divider />
          </React.Fragment>
        ))}
      </List>
      <Box sx={{ mt: 4, textAlign: 'right' }}>
        <Typography variant="h6" gutterBottom>
          Total: ${getTotalPrice().toFixed(2)}
        </Typography>
        <Button
          variant="contained"
          color="primary"
          onClick={() => navigate('/checkout')}
          sx={{ mr: 2 }}
        >
          Proceed to Checkout
        </Button>
        <Button
          variant="outlined"
          color="secondary"
          onClick={clearCart}
        >
          Clear Cart
        </Button>
      </Box>
    </Container>
  );
}

export default Cart; 