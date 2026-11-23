# 00aedec4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aeddfc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeddfc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-f8668906b56c56a240573331ddd8f769)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aedf08`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedf08.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-98f84e53448277453bc711feacb475e3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedec4",
  "name": "_ZN8firebase4util3uri11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e87d56099b0492c6fafc4780f921002f31800944661317bed4a788b534dc8de",
  "source_text_sha256": "0e87d56099b0492c6fafc4780f921002f31800944661317bed4a788b534dc8de",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedec4",
        "00aedeff"
      ]
    ],
    "bytes_sha256": "5af3d7f0a6063acd89c7495194b0ee73703768ea13820548de2b8cb3f8eb5fc3",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 203 bytes

~~~c

undefined8 _ZN8firebase4util3uri11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_010a0a30)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedec4"></a> `00aedec4` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedec8"></a> `00aedec8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedecc"></a> `00aedecc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeded0"></a> `00aeded0` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aeded4"></a> `00aeded4` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00aeded8"></a> `00aeded8` | `8b 00 00 54` | b.lt 0x00aedee8 | `CONDITIONAL_JUMP`
<a id="insn-00aededc"></a> `00aededc` | `40 bd ff f0` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00aedee0"></a> `00aedee0` | `00 50 17 91` | add x0,x0,#0x5d4 | `FALL_THROUGH`
<a id="insn-00aedee4"></a> `00aedee4` | `93 c0 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00aedee8"></a> `00aedee8` | `88 2d 00 f0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedeec"></a> `00aedeec` | `08 c1 28 91` | add x8,x8,#0xa30 | `FALL_THROUGH`
<a id="insn-00aedef0"></a> `00aedef0` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aedef4"></a> `00aedef4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedef8"></a> `00aedef8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aedefc"></a> `00aedefc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedec4`](#insn-00aedec4) 範囲 `[['00aedec4', '00aededb']]`
  - `CONDITIONAL_JUMP` [`00aeded8`](#insn-00aeded8) → [`00aedee8`](#insn-00aedee8)
  - `FALL_THROUGH` [`00aeded8`](#insn-00aeded8) → [`00aededc`](#insn-00aededc)
- ブロック [`00aededc`](#insn-00aededc) 範囲 `[['00aededc', '00aedee7']]`
  - `FALL_THROUGH` [`00aedee4`](#insn-00aedee4) → [`00aedee8`](#insn-00aedee8)
- ブロック [`00aedee8`](#insn-00aedee8) 範囲 `[['00aedee8', '00aedeff']]`

## 命令位置別の参照

- [`00aedec4`](#insn-00aedec4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedec8`](#insn-00aedec8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeded8`](#insn-00aeded8) → [`00aedee8`](#insn-00aedee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedee0`](#insn-00aedee0) → `002985d4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedee4`](#insn-00aedee4) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00aedef0`](#insn-00aedef0) → `010a0a30`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedef4`](#insn-00aedef4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedec4`](#insn-00aedec4)

~~~json
{
  "source": "00aedec4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedec8`](#insn-00aedec8)

~~~json
{
  "source": "00aedec8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeded8`](#insn-00aeded8)

~~~json
{
  "source": "00aeded8",
  "target": "00aedee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedee0`](#insn-00aedee0)

~~~json
{
  "source": "00aedee0",
  "target": "002985d4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002985d4",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002985d4",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedee4`](#insn-00aedee4)

~~~json
{
  "source": "00aedee4",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedef0`](#insn-00aedef0)

~~~json
{
  "source": "00aedef0",
  "target": "010a0a30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedef4`](#insn-00aedef4)

~~~json
{
  "source": "00aedef4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
