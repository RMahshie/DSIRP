Deck merge_sort(const Deck& deck) {
    if (deck.size() <= 1) {
        // base case: deck is already sorted
        return deck;
    } else {
        // find the midpoint of the deck
        int midpoint = deck.size() / 2;

        // divide the deck into two subdecks
        Deck left_half(deck.begin(), deck.begin() + midpoint);
        Deck right_half(deck.begin() + midpoint, deck.end());

        // sort the subdecks using sort
        left_half = merge_sort(left_half);
        right_half = merge_sort(right_half);

        // merge the two halves and return the result
        return merge(left_half, right_half);
    }
}
