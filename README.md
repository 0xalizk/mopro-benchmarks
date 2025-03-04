### Benchmarks

Plots for [mopro](https://zkmopro.org/docs/performance) client-side proving

```
uv init
uv add matplotlib toml
uv run src/main.py data/[toml file]
```

<table>
  <tr>
    <td><img src="plots/circom.android.proof.gen.png" width="400"><br>Circom Android Proof Generation</td>
    <td><img src="plots/circom.android.wit.gen.png" width="400"><br>Circom Android Witness Generation</td>
  </tr>
  <tr>
    <td><img src="plots/circom.ios.proof.gen.png" width="400"><br>Circom iOS Proof Generation</td>
    <td><img src="plots/circom.ios.wit.gen.png" width="400"><br>Circom iOS Witness Generation</td>
  </tr>
  <tr>
    <td><img src="plots/circom.macos.proof.gen.png" width="400"><br>Circom MacOS Proof Generation</td>
    <td><img src="plots/circom.macos.wit.gen.png" width="400"><br>Circom MacOS Witness Generation</td>
  </tr>
  <tr>
    <td><img src="plots/halo2.keccak.proof.gen.png" width="400"><br>Halo2 Keccak Proof Generation</td>
    <td><img src="plots/halo2.rsa.proof.gen.png" width="400"><br>Halo2 RSA Proof Generation</td>
  </tr>
</table>

