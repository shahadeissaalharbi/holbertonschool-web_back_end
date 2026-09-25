export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  map.forEach((quantity, key) => {
    if (quantity === 1) {
      map.set(key, 100);
    }
  });
  return map;
}
