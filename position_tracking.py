class PositionTracker:
    def __init__(self):
        self.positions = {}

    def add_position(self, symbol, quantity, entry_price):
        self.positions[symbol] = {'quantity': quantity, 'entry_price': entry_price}

    def remove_position(self, symbol):
        if symbol in self.positions:
            del self.positions[symbol]

    def update_position(self, symbol, price):
        if symbol in self.positions:
            self.positions[symbol]['current_price'] = price
            return self.positions[symbol]
        return None

    def get_positions(self):
        return self.positions
