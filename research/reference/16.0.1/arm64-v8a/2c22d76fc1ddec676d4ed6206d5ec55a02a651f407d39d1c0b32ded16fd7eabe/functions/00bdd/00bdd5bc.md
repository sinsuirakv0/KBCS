# 00bdd5bc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdd194`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdd194.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-4aa626d08391f719f0c5196a0a0d9306)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdd658`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdd/00bdd658.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-4b2a95165d01c7d2db492924615d88a5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdd5bc",
  "name": "_ZN8firebase4auth8userinfo15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "71487d112618fce376859e9534f4a85012c4403cef8b4d6f7de8d54846bcfa7a",
  "source_text_sha256": "71487d112618fce376859e9534f4a85012c4403cef8b4d6f7de8d54846bcfa7a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdd5bc",
        "00bdd627"
      ]
    ],
    "bytes_sha256": "ed6d0aadd88d8536b02598d06bf05f40b8874b279c6c882e124406eaba361ff5",
    "instruction_count": 27,
    "instruction_bytes": 108,
    "body_bytes": 108,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af60](../00c5a/00c5af60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 483 bytes

~~~c

bool _ZN8firebase4auth8userinfo15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01126db8 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126db0,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126db8 = iVar2 == 0;
    bVar1 = (bool)DAT_01126db8;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdd5bc"></a> `00bdd5bc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdd5c0"></a> `00bdd5c0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd5c4"></a> `00bdd5c4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdd5c8"></a> `00bdd5c8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdd5cc"></a> `00bdd5cc` | `55 2a 00 b0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdd5d0"></a> `00bdd5d0` | `a8 e2 76 39` | ldrb w8,[x21, #0xdb8] | `FALL_THROUGH`
<a id="insn-00bdd5d4"></a> `00bdd5d4` | `68 00 00 34` | cbz w8,0x00bdd5e0 | `CONDITIONAL_JUMP`
<a id="insn-00bdd5d8"></a> `00bdd5d8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bdd5dc"></a> `00bdd5dc` | `0f 00 00 14` | b 0x00bdd618 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdd5e0"></a> `00bdd5e0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdd5e4"></a> `00bdd5e4` | `49 2a 00 b0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdd5e8"></a> `00bdd5e8` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bdd5ec"></a> `00bdd5ec` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bdd5f0"></a> `00bdd5f0` | `21 d9 46 f9` | ldr x1,[x9, #0xdb0] | `FALL_THROUGH`
<a id="insn-00bdd5f4"></a> `00bdd5f4` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bdd5f8"></a> `00bdd5f8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdd5fc"></a> `00bdd5fc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdd600"></a> `00bdd600` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bdd604"></a> `00bdd604` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdd608"></a> `00bdd608` | `56 f6 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdd60c"></a> `00bdd60c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bdd610"></a> `00bdd610` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bdd614"></a> `00bdd614` | `a0 e2 36 39` | strb w0,[x21, #0xdb8] | `FALL_THROUGH`
<a id="insn-00bdd618"></a> `00bdd618` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdd61c"></a> `00bdd61c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdd620"></a> `00bdd620` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdd624"></a> `00bdd624` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdd5bc`](#insn-00bdd5bc) 範囲 `[['00bdd5bc', '00bdd5d7']]`
  - `CONDITIONAL_JUMP` [`00bdd5d4`](#insn-00bdd5d4) → [`00bdd5e0`](#insn-00bdd5e0)
  - `FALL_THROUGH` [`00bdd5d4`](#insn-00bdd5d4) → [`00bdd5d8`](#insn-00bdd5d8)
- ブロック [`00bdd5d8`](#insn-00bdd5d8) 範囲 `[['00bdd5d8', '00bdd5df']]`
  - `UNCONDITIONAL_JUMP` [`00bdd5dc`](#insn-00bdd5dc) → [`00bdd618`](#insn-00bdd618)
- ブロック [`00bdd5e0`](#insn-00bdd5e0) 範囲 `[['00bdd5e0', '00bdd617']]`
  - `FALL_THROUGH` [`00bdd614`](#insn-00bdd614) → [`00bdd618`](#insn-00bdd618)
- ブロック [`00bdd618`](#insn-00bdd618) 範囲 `[['00bdd618', '00bdd627']]`

## 命令位置別の参照

- [`00bdd5bc`](#insn-00bdd5bc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd5c0`](#insn-00bdd5c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd5c4`](#insn-00bdd5c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd5d0`](#insn-00bdd5d0) → `01126db8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdd5d4`](#insn-00bdd5d4) → [`00bdd5e0`](#insn-00bdd5e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd5dc`](#insn-00bdd5dc) → [`00bdd618`](#insn-00bdd618) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd5f0`](#insn-00bdd5f0) → `01126db0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdd608`](#insn-00bdd608) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bdd614`](#insn-00bdd614) → `01126db8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdd618`](#insn-00bdd618) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdd61c`](#insn-00bdd61c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdd5bc`](#insn-00bdd5bc)

~~~json
{
  "source": "00bdd5bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd5c0`](#insn-00bdd5c0)

~~~json
{
  "source": "00bdd5c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd5c4`](#insn-00bdd5c4)

~~~json
{
  "source": "00bdd5c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd5d0`](#insn-00bdd5d0)

~~~json
{
  "source": "00bdd5d0",
  "target": "01126db8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126db8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd5d4`](#insn-00bdd5d4)

~~~json
{
  "source": "00bdd5d4",
  "target": "00bdd5e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd5dc`](#insn-00bdd5dc)

~~~json
{
  "source": "00bdd5dc",
  "target": "00bdd618",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd5f0`](#insn-00bdd5f0)

~~~json
{
  "source": "00bdd5f0",
  "target": "01126db0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126db0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd608`](#insn-00bdd608)

~~~json
{
  "source": "00bdd608",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdd614`](#insn-00bdd614)

~~~json
{
  "source": "00bdd614",
  "target": "01126db8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126db8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdd618`](#insn-00bdd618)

~~~json
{
  "source": "00bdd618",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdd61c`](#insn-00bdd61c)

~~~json
{
  "source": "00bdd61c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
