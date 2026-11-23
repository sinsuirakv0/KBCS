# 00acd8ac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acd7e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd7e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-999fe11f539bbc1673611accc36ebc27)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acd8f0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acd8f0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-b1899bb0b1ccb737d8ed34e51bbf8fa6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acd8ac",
  "name": "FUN_00acd8ac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c7e2b6aebdcf688cad29ecacd582b15328ced32f8212d8752354bf4dc78f24a5",
  "source_text_sha256": "c7e2b6aebdcf688cad29ecacd582b15328ced32f8212d8752354bf4dc78f24a5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acd8ac",
        "00acd8eb"
      ]
    ],
    "bytes_sha256": "74c92edb42e0bd7f58b96ffda328cb97e47cbdc0818379504505a37f68aed3cd",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 549 bytes

~~~c

void FUN_00acd8ac(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c0f7f8;
  param_2[1] = uVar1;
  if ((*(byte *)(param_1 + 0x10) & 1) == 0) {
    uVar2 = *(undefined8 *)(param_1 + 0x18);
    uVar1 = *(undefined8 *)(param_1 + 0x10);
    param_2[4] = *(undefined8 *)(param_1 + 0x20);
    param_2[3] = uVar2;
    param_2[2] = uVar1;
    return;
  }
  FUN_00418fe0(param_2 + 2,*(undefined8 *)(param_1 + 0x20),*(undefined8 *)(param_1 + 0x18));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acd8ac"></a> `00acd8ac` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00acd8b0"></a> `00acd8b0` | `09 0a 00 d0` | adrp x9,0xc0f000 | `FALL_THROUGH`
<a id="insn-00acd8b4"></a> `00acd8b4` | `29 e1 1f 91` | add x9,x9,#0x7f8 | `FALL_THROUGH`
<a id="insn-00acd8b8"></a> `00acd8b8` | `29 20 00 a9` | stp x9,x8,[x1] | `FALL_THROUGH`
<a id="insn-00acd8bc"></a> `00acd8bc` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00acd8c0"></a> `00acd8c0` | `09 0d 41 38` | ldrb w9,[x8, #0x10]! | `FALL_THROUGH`
<a id="insn-00acd8c4"></a> `00acd8c4` | `c9 00 00 37` | tbnz w9,#0x0,0x00acd8dc | `CONDITIONAL_JUMP`
<a id="insn-00acd8c8"></a> `00acd8c8` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acd8cc"></a> `00acd8cc` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00acd8d0"></a> `00acd8d0` | `29 00 02 f8` | stur x9,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00acd8d4"></a> `00acd8d4` | `20 00 81 3c` | stur q0,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00acd8d8"></a> `00acd8d8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acd8dc"></a> `00acd8dc` | `02 a0 41 a9` | ldp x2,x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00acd8e0"></a> `00acd8e0` | `20 40 00 91` | add x0,x1,#0x10 | `FALL_THROUGH`
<a id="insn-00acd8e4"></a> `00acd8e4` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00acd8e8"></a> `00acd8e8` | `be 2d e5 17` | b 0x00418fe0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acd8ac`](#insn-00acd8ac) 範囲 `[['00acd8ac', '00acd8c7']]`
  - `CONDITIONAL_JUMP` [`00acd8c4`](#insn-00acd8c4) → [`00acd8dc`](#insn-00acd8dc)
  - `FALL_THROUGH` [`00acd8c4`](#insn-00acd8c4) → [`00acd8c8`](#insn-00acd8c8)
- ブロック [`00acd8c8`](#insn-00acd8c8) 範囲 `[['00acd8c8', '00acd8db']]`
- ブロック [`00acd8dc`](#insn-00acd8dc) 範囲 `[['00acd8dc', '00acd8eb']]`

## 命令位置別の参照

- [`00acd8b8`](#insn-00acd8b8) → `00c0f7f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acd8c4`](#insn-00acd8c4) → [`00acd8dc`](#insn-00acd8dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acd8e8`](#insn-00acd8e8) → [`00418fe0`](../00418/00418fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418fe0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acd8b8`](#insn-00acd8b8)

~~~json
{
  "source": "00acd8b8",
  "target": "00c0f7f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f7f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acd8c4`](#insn-00acd8c4)

~~~json
{
  "source": "00acd8c4",
  "target": "00acd8dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acd8e8`](#insn-00acd8e8)

~~~json
{
  "source": "00acd8e8",
  "target": "00418fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
