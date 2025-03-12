### Benchmarks

Plots for [mopro](https://zkmopro.org/docs/performance) client-side proving

```
uv init
uv add matplotlib toml
uv run src/main.py data/[toml file]
```

### Notes
- Depending on the data source, you can set `transpose` to true for convenience (in `/data/[toml file]`), which transposes `dataset`
- Changint `y_ticks` in `/data/[toml file]` does affect how "stretched" the bars are. You may want to include a lower tick to better dilineate low-value perf benchs, while leaving their corresponding `y_tickslabels` empty "" to reduce crowding
  - Take a look at different [scales](/scale) 
- To change the grouping of the bars, one can swap `rows` and `columns` and flip the `transpose` value in the toml file (to see this, diff a `data/*_by.bench.toml` and the corresponding `data/*_by.poroject.toml` files)

<br>

<table>
  <tr>
    <td><img src="plots/circom.android.proof.gen_by.bench.png" width="400"><br>Circom Android Proof Generation</td>
    <td><img src="plots/circom.android.wit.gen_by.bench.png" width="400"><br>Circom Android Witness Generation</td>
  </tr>
  <tr>
    <td><img src="plots/circom.ios.proof.gen_by.bench.png" width="400"><br>Circom iOS Proof Generation</td>
    <td><img src="plots/circom.ios.wit.gen_by.bench.png" width="400"><br>Circom iOS Witness Generation</td>
  </tr>
  <tr>
    <td><img src="plots/circom.macos.proof.gen_by.bench.png" width="400"><br>Circom MacOS Proof Generation</td>
    <td><img src="plots/circom.macos.wit.gen_by.bench.png" width="400"><br>Circom MacOS Witness Generation</td>
  </tr>
  <tr>
    <td><img src="plots/halo2.keccak.proof.gen_by.bench.png" width="400"><br>Halo2 Keccak Proof Generation</td>
    <td><img src="plots/halo2.rsa.proof.gen_by.bench.png" width="400"><br>Halo2 RSA Proof Generation</td>
  </tr>
</table>

