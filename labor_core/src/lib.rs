use pyo3::prelude::*;

#[pyfunction]
fn calculate_total_value(items: Vec<(f64, i32)>) -> PyResult<f64> {
    let total: f64 = items.iter()
        .map(|(price, quantity)| price * *quantity as f64)
        .sum();
    Ok(total)
}

#[pymodule]
fn labor_core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(calculate_total_value, m)?)?;
    Ok(())
}