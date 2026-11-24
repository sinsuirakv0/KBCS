# 00bdce4c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6d94c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d94c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-572e26b801df3bcefdad55f2200ac99a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdd274`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd274.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-118291f13241dc6e0155566ce69ce2c5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdce4c",
  "name": "_ZN8firebase4auth4user15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5a78789154684e0098376f9657a5bb05d44fc0ff39534db2ea56051dfcbb46e5",
  "source_text_sha256": "5a78789154684e0098376f9657a5bb05d44fc0ff39534db2ea56051dfcbb46e5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdce4c",
        "00bdceb7"
      ]
    ],
    "bytes_sha256": "e23dfac19495fbc6bc9aa1278a5412c8a203e366e0a208e62ef363b10e05f8a2",
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

- [00c5ab60](../00c5a/00c5ab60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 479 bytes

~~~c

bool _ZN8firebase4auth4user15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_01126928 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_01126920,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_01126928 = iVar2 == 0;
    bVar1 = (bool)DAT_01126928;
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
<a id="insn-00bdce4c"></a> `00bdce4c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdce50"></a> `00bdce50` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdce54"></a> `00bdce54` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdce58"></a> `00bdce58` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdce5c"></a> `00bdce5c` | `55 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdce60"></a> `00bdce60` | `a8 a2 64 39` | ldrb w8,[x21, #0x928] | `FALL_THROUGH`
<a id="insn-00bdce64"></a> `00bdce64` | `68 00 00 34` | cbz w8,0x00bdce70 | `CONDITIONAL_JUMP`
<a id="insn-00bdce68"></a> `00bdce68` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bdce6c"></a> `00bdce6c` | `0f 00 00 14` | b 0x00bdcea8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdce70"></a> `00bdce70` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdce74"></a> `00bdce74` | `49 2a 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdce78"></a> `00bdce78` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bdce7c"></a> `00bdce7c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bdce80"></a> `00bdce80` | `21 91 44 f9` | ldr x1,[x9, #0x920] | `FALL_THROUGH`
<a id="insn-00bdce84"></a> `00bdce84` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bdce88"></a> `00bdce88` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdce8c"></a> `00bdce8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdce90"></a> `00bdce90` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bdce94"></a> `00bdce94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdce98"></a> `00bdce98` | `32 f7 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdce9c"></a> `00bdce9c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bdcea0"></a> `00bdcea0` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bdcea4"></a> `00bdcea4` | `a0 a2 24 39` | strb w0,[x21, #0x928] | `FALL_THROUGH`
<a id="insn-00bdcea8"></a> `00bdcea8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdceac"></a> `00bdceac` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdceb0"></a> `00bdceb0` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdceb4"></a> `00bdceb4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdce4c`](#insn-00bdce4c) 範囲 `[['00bdce4c', '00bdce67']]`
  - `CONDITIONAL_JUMP` [`00bdce64`](#insn-00bdce64) → [`00bdce70`](#insn-00bdce70)
  - `FALL_THROUGH` [`00bdce64`](#insn-00bdce64) → [`00bdce68`](#insn-00bdce68)
- ブロック [`00bdce68`](#insn-00bdce68) 範囲 `[['00bdce68', '00bdce6f']]`
  - `UNCONDITIONAL_JUMP` [`00bdce6c`](#insn-00bdce6c) → [`00bdcea8`](#insn-00bdcea8)
- ブロック [`00bdce70`](#insn-00bdce70) 範囲 `[['00bdce70', '00bdcea7']]`
  - `FALL_THROUGH` [`00bdcea4`](#insn-00bdcea4) → [`00bdcea8`](#insn-00bdcea8)
- ブロック [`00bdcea8`](#insn-00bdcea8) 範囲 `[['00bdcea8', '00bdceb7']]`

## 命令位置別の参照

- [`00bdce4c`](#insn-00bdce4c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce50`](#insn-00bdce50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce54`](#insn-00bdce54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce60`](#insn-00bdce60) → `01126928`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdce64`](#insn-00bdce64) → [`00bdce70`](#insn-00bdce70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce6c`](#insn-00bdce6c) → [`00bdcea8`](#insn-00bdcea8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce80`](#insn-00bdce80) → `01126920`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdce98`](#insn-00bdce98) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bdcea4`](#insn-00bdcea4) → `01126928`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdcea8`](#insn-00bdcea8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdceac`](#insn-00bdceac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdce4c`](#insn-00bdce4c)

~~~json
{
  "source": "00bdce4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce50`](#insn-00bdce50)

~~~json
{
  "source": "00bdce50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce54`](#insn-00bdce54)

~~~json
{
  "source": "00bdce54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce60`](#insn-00bdce60)

~~~json
{
  "source": "00bdce60",
  "target": "01126928",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126928",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdce64`](#insn-00bdce64)

~~~json
{
  "source": "00bdce64",
  "target": "00bdce70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce6c`](#insn-00bdce6c)

~~~json
{
  "source": "00bdce6c",
  "target": "00bdcea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce80`](#insn-00bdce80)

~~~json
{
  "source": "00bdce80",
  "target": "01126920",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126920",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdce98`](#insn-00bdce98)

~~~json
{
  "source": "00bdce98",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcea4`](#insn-00bdcea4)

~~~json
{
  "source": "00bdcea4",
  "target": "01126928",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126928",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcea8`](#insn-00bdcea8)

~~~json
{
  "source": "00bdcea8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdceac`](#insn-00bdceac)

~~~json
{
  "source": "00bdceac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
