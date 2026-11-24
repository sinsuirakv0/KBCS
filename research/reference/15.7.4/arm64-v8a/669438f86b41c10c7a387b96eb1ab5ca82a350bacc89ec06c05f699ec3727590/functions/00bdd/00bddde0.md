# 00bddde0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddd90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-bfecccbecd4a861cf604e6392ac0320b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a840`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a840.md) · 移動量 `+0x7ca60`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0012.md#compare-73c771c14375c7b63f7ce956435ebb57)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddde0",
  "name": "_ZN8firebase26ReferenceCountedFutureImplC2Em",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1e75e3e83802a3196f8e1c8a4119cfec03277145d92e5768bfef47e27d27bc9f",
  "source_text_sha256": "1e75e3e83802a3196f8e1c8a4119cfec03277145d92e5768bfef47e27d27bc9f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddde0",
        "00bdddef"
      ]
    ],
    "bytes_sha256": "373c7e0bbeb80ddc59ad79005ad52b162fc2435e8ede940bf36d9a9d0b26c0bd",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae00d8](../00ae0/00ae00d8.md)
- [00b01390](../00b01/00b01390.md)
- [00b02374](../00b02/00b02374.md)
- [00b02510](../00b02/00b02510.md)
- [00b0d784](../00b0d/00b0d784.md)
- [00b49470](../00b49/00b49470.md)
- [00b524ec](../00b52/00b524ec.md)
- [00b54b38](../00b54/00b54b38.md)
- [00b5af8c](../00b5a/00b5af8c.md)

## 呼び出し先

- [00ae020c](../00ae0/00ae020c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 147 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImplC2Em(void)

{
  (*(code *)PTR__ZN8firebase26ReferenceCountedFutureImplC2Em_00c1d7a8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddde0"></a> `00bddde0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddde4"></a> `00bddde4` | `11 d6 43 f9` | ldr x17,[x16, #0x7a8] | `FALL_THROUGH`
<a id="insn-00bddde8"></a> `00bddde8` | `10 a2 1e 91` | add x16,x16,#0x7a8 | `FALL_THROUGH`
<a id="insn-00bdddec"></a> `00bdddec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddde0`](#insn-00bddde0) 範囲 `[['00bddde0', '00bdddef']]`

## 命令位置別の参照

- [`00bddde4`](#insn-00bddde4) → `00c1d7a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdddec`](#insn-00bdddec) → [`00ae020c`](../00ae0/00ae020c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae020c` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImplC2Em` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddde4`](#insn-00bddde4)

~~~json
{
  "source": "00bddde4",
  "target": "00c1d7a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d7a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdddec`](#insn-00bdddec)

~~~json
{
  "source": "00bdddec",
  "target": "00ae020c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
