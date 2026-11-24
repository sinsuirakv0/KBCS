# 00bd7fec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b68aec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b68/00b68aec.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-c61dbdcefb2571d57af9bd59cdaa6767)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd8414`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd8/00bd8414.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0011.md#compare-c64d16f1f3346a13ca8a79d3f564d4d5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd7fec",
  "name": "_ZN8firebase4auth15phonecredential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae01b625eb14b93ea6e2881227be1a537f19a53a626b7efeed06d121db07d9f7",
  "source_text_sha256": "ae01b625eb14b93ea6e2881227be1a537f19a53a626b7efeed06d121db07d9f7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd7fec",
        "00bd8057"
      ]
    ],
    "bytes_sha256": "0cf8c8ea33c74a036e6f2f02a33f119166cfba9997d3fd87956cbb016abc7160",
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

## 疑似コード / UTF-8 588 bytes

~~~c

bool _ZN8firebase4auth15phonecredential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  bool bVar1;
  int iVar2;
  
  if (DAT_011268e0 == '\0') {
    iVar2 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_011268d8,param_2,param_3);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    DAT_011268e0 = iVar2 == 0;
    bVar1 = (bool)DAT_011268e0;
  }
  else {
    bVar1 = false;
  }
                    /* try { // try from 00bd8054 to 00cd806f has its CatchHandler @ 00bdee40 */
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd7fec"></a> `00bd7fec` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd7ff0"></a> `00bd7ff0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd7ff4"></a> `00bd7ff4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd7ff8"></a> `00bd7ff8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd7ffc"></a> `00bd7ffc` | `75 2a 00 f0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd8000"></a> `00bd8000` | `a8 82 63 39` | ldrb w8,[x21, #0x8e0] | `FALL_THROUGH`
<a id="insn-00bd8004"></a> `00bd8004` | `68 00 00 34` | cbz w8,0x00bd8010 | `CONDITIONAL_JUMP`
<a id="insn-00bd8008"></a> `00bd8008` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bd800c"></a> `00bd800c` | `0f 00 00 14` | b 0x00bd8048 | `UNCONDITIONAL_JUMP`
<a id="insn-00bd8010"></a> `00bd8010` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd8014"></a> `00bd8014` | `69 2a 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd8018"></a> `00bd8018` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00bd801c"></a> `00bd801c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00bd8020"></a> `00bd8020` | `21 6d 44 f9` | ldr x1,[x9, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bd8024"></a> `00bd8024` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bd8028"></a> `00bd8028` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd802c"></a> `00bd802c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd8030"></a> `00bd8030` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bd8034"></a> `00bd8034` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd8038"></a> `00bd8038` | `ca 0a 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bd803c"></a> `00bd803c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bd8040"></a> `00bd8040` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bd8044"></a> `00bd8044` | `a0 82 23 39` | strb w0,[x21, #0x8e0] | `FALL_THROUGH`
<a id="insn-00bd8048"></a> `00bd8048` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd804c"></a> `00bd804c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd8050"></a> `00bd8050` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd8054"></a> `00bd8054` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd7fec`](#insn-00bd7fec) 範囲 `[['00bd7fec', '00bd8007']]`
  - `CONDITIONAL_JUMP` [`00bd8004`](#insn-00bd8004) → [`00bd8010`](#insn-00bd8010)
  - `FALL_THROUGH` [`00bd8004`](#insn-00bd8004) → [`00bd8008`](#insn-00bd8008)
- ブロック [`00bd8008`](#insn-00bd8008) 範囲 `[['00bd8008', '00bd800f']]`
  - `UNCONDITIONAL_JUMP` [`00bd800c`](#insn-00bd800c) → [`00bd8048`](#insn-00bd8048)
- ブロック [`00bd8010`](#insn-00bd8010) 範囲 `[['00bd8010', '00bd8047']]`
  - `FALL_THROUGH` [`00bd8044`](#insn-00bd8044) → [`00bd8048`](#insn-00bd8048)
- ブロック [`00bd8048`](#insn-00bd8048) 範囲 `[['00bd8048', '00bd8053']]`
  - `FALL_THROUGH` [`00bd8050`](#insn-00bd8050) → [`00bd8054`](#insn-00bd8054)
- ブロック [`00bd8054`](#insn-00bd8054) 範囲 `[['00bd8054', '00bd8057']]`

## 命令位置別の参照

- [`00bd7fec`](#insn-00bd7fec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7ff0`](#insn-00bd7ff0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7ff4`](#insn-00bd7ff4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd8000`](#insn-00bd8000) → `011268e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd8004`](#insn-00bd8004) → [`00bd8010`](#insn-00bd8010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd800c`](#insn-00bd800c) → [`00bd8048`](#insn-00bd8048) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd8020`](#insn-00bd8020) → `011268d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd8038`](#insn-00bd8038) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bd8044`](#insn-00bd8044) → `011268e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd8048`](#insn-00bd8048) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd804c`](#insn-00bd804c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd7fec`](#insn-00bd7fec)

~~~json
{
  "source": "00bd7fec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7ff0`](#insn-00bd7ff0)

~~~json
{
  "source": "00bd7ff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7ff4`](#insn-00bd7ff4)

~~~json
{
  "source": "00bd7ff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd8000`](#insn-00bd8000)

~~~json
{
  "source": "00bd8000",
  "target": "011268e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd8004`](#insn-00bd8004)

~~~json
{
  "source": "00bd8004",
  "target": "00bd8010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd800c`](#insn-00bd800c)

~~~json
{
  "source": "00bd800c",
  "target": "00bd8048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd8020`](#insn-00bd8020)

~~~json
{
  "source": "00bd8020",
  "target": "011268d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd8038`](#insn-00bd8038)

~~~json
{
  "source": "00bd8038",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd8044`](#insn-00bd8044)

~~~json
{
  "source": "00bd8044",
  "target": "011268e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd8048`](#insn-00bd8048)

~~~json
{
  "source": "00bd8048",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd804c`](#insn-00bd804c)

~~~json
{
  "source": "00bd804c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
