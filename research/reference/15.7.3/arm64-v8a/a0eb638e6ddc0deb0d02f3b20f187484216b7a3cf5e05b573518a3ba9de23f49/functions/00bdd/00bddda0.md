# 00bddda0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddcf0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddcf0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-4f55ed2b4c44baa10187270cb1afcd06)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdddf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-ca5aac789fdbd464d9b1f075e4b6c9b4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddda0",
  "name": "_ZN8firebase26ReferenceCountedFutureImplD1Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "063313d10474bee1f1d017551f8a368159a5242432adbdc44e479b52efc1d9ff",
  "source_text_sha256": "063313d10474bee1f1d017551f8a368159a5242432adbdc44e479b52efc1d9ff",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddda0",
        "00bdddaf"
      ]
    ],
    "bytes_sha256": "bc36b2437d0f56e697d4fc4254742e0549bb382a951f929975e03c3072a10802",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae00e4](../00ae0/00ae00e4.md)
- [00b013b0](../00b01/00b013b0.md)
- [00b01410](../00b01/00b01410.md)
- [00b0221c](../00b02/00b0221c.md)
- [00b0d740](../00b0d/00b0d740.md)
- [00b0db4c](../00b0d/00b0db4c.md)
- [00b4947c](../00b49/00b4947c.md)
- [00b524f8](../00b52/00b524f8.md)
- [00b557f4](../00b55/00b557f4.md)
- [00b5b32c](../00b5b/00b5b32c.md)

## 呼び出し先

- [00afeae0](../00afe/00afeae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 147 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImplD1Ev(void)

{
  (*(code *)PTR__ZN8firebase26ReferenceCountedFutureImplD1Ev_00c1d760)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddda0"></a> `00bddda0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddda4"></a> `00bddda4` | `11 b2 43 f9` | ldr x17,[x16, #0x760] | `FALL_THROUGH`
<a id="insn-00bddda8"></a> `00bddda8` | `10 82 1d 91` | add x16,x16,#0x760 | `FALL_THROUGH`
<a id="insn-00bdddac"></a> `00bdddac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddda0`](#insn-00bddda0) 範囲 `[['00bddda0', '00bdddaf']]`

## 命令位置別の参照

- [`00bddda4`](#insn-00bddda4) → `00c1d760`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdddac`](#insn-00bdddac) → [`00afeae0`](../00afe/00afeae0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afeae0` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImplD1Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddda4`](#insn-00bddda4)

~~~json
{
  "source": "00bddda4",
  "target": "00c1d760",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d760",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdddac`](#insn-00bdddac)

~~~json
{
  "source": "00bdddac",
  "target": "00afeae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
