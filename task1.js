function averageOfFiltered(numbers) {
    const filtered = numbers.filter(num => num > 50);
    const sum = filtered.reduce((acc, num) => acc + num, 0);
    return filtered.length > 0 ? sum / filtered.length : 0;
}

//convert to python
def average_of_filtered(numbers):
    filtered = [num for num in numbers if num > 50]
    total = sum(filtered)
    return total / len(filtered) if filtered else 0

