# 00b0cefc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b0ce34`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b0c/00b0ce34.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-7ef161438b1fc9030a538a3d550fec8e)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b0cf40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0c/00b0cf40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0009.md#compare-36fd7fcaed168b19dca8b52b6182d87c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0cefc",
  "name": "_ZN11flatbuffers17FlatBufferBuilderD2Ev",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b2d0c2a69615f351f05fb1bd406710d603d61a2e60a52c95db6b488801fd7b5c",
  "source_text_sha256": "b2d0c2a69615f351f05fb1bd406710d603d61a2e60a52c95db6b488801fd7b5c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0cefc",
        "00b0cf87"
      ]
    ],
    "bytes_sha256": "4770abc239f6dd61b1a9f437a4aa0a771a9af93d84a4fff2f70436c36d2b71c3",
    "instruction_count": 35,
    "instruction_bytes": 140,
    "body_bytes": 140,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00bdea10](../00bde/00bdea10.md)

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdeb10](../00bde/00bdeb10.md)
- [00bdef40](../00bde/00bdef40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 944 bytes

~~~c

void _ZN11flatbuffers17FlatBufferBuilderD2Ev(long *param_1)

{
  long *plVar1;
  void *pvVar2;
  
  pvVar2 = (void *)param_1[0xb];
  if (pvVar2 != (void *)0x0) {
    _ZNSt6__ndk16__treeIN11flatbuffers6OffsetINS1_6StringEEENS1_17FlatBufferBuilder19StringOffsetCompareENS_9allocatorIS4_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
              (pvVar2,*(undefined8 *)((long)pvVar2 + 8));
    _ZdlPv(pvVar2);
  }
  pvVar2 = (void *)param_1[5];
                    /* try { // try from 00b0cf2c to 00c0cf33 has its CatchHandler @ 00b0cfa4 */
  if (pvVar2 != (void *)0x0) {
    plVar1 = (long *)*param_1;
    if (plVar1 == (long *)0x0) {
      _ZdaPv(pvVar2);
    }
    else {
      (**(code **)(*plVar1 + 0x18))(plVar1,pvVar2,param_1[4]);
    }
  }
  param_1[5] = 0;
  if (((char)param_1[1] != '\0') && ((long *)*param_1 != (long *)0x0)) {
    (**(code **)(*(long *)*param_1 + 8))();
  }
  *param_1 = 0;
  *(undefined1 *)(param_1 + 1) = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b0cefc"></a> `00b0cefc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b0cf00"></a> `00b0cf00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cf04"></a> `00b0cf04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b0cf08"></a> `00b0cf08` | `14 2c 40 f9` | ldr x20,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00b0cf0c"></a> `00b0cf0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b0cf10"></a> `00b0cf10` | `d4 00 00 b4` | cbz x20,0x00b0cf28 | `CONDITIONAL_JUMP`
<a id="insn-00b0cf14"></a> `00b0cf14` | `81 06 40 f9` | ldr x1,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b0cf18"></a> `00b0cf18` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0cf1c"></a> `00b0cf1c` | `fd 46 03 94` | bl 0x00bdeb10 | `UNCONDITIONAL_CALL`
<a id="insn-00b0cf20"></a> `00b0cf20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b0cf24"></a> `00b0cf24` | `3b 38 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00b0cf28"></a> `00b0cf28` | `61 16 40 f9` | ldr x1,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b0cf2c"></a> `00b0cf2c` | `41 01 00 b4` | cbz x1,0x00b0cf54 | `CONDITIONAL_JUMP`
<a id="insn-00b0cf30"></a> `00b0cf30` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00b0cf34"></a> `00b0cf34` | `c0 00 00 b4` | cbz x0,0x00b0cf4c | `CONDITIONAL_JUMP`
<a id="insn-00b0cf38"></a> `00b0cf38` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b0cf3c"></a> `00b0cf3c` | `62 12 40 f9` | ldr x2,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b0cf40"></a> `00b0cf40` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00b0cf44"></a> `00b0cf44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b0cf48"></a> `00b0cf48` | `03 00 00 14` | b 0x00b0cf54 | `UNCONDITIONAL_JUMP`
<a id="insn-00b0cf4c"></a> `00b0cf4c` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00b0cf50"></a> `00b0cf50` | `fc 47 03 94` | bl 0x00bdef40 | `UNCONDITIONAL_CALL`
<a id="insn-00b0cf54"></a> `00b0cf54` | `68 22 40 39` | ldrb w8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b0cf58"></a> `00b0cf58` | `7f 16 00 f9` | str xzr,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b0cf5c"></a> `00b0cf5c` | `c8 00 00 34` | cbz w8,0x00b0cf74 | `CONDITIONAL_JUMP`
<a id="insn-00b0cf60"></a> `00b0cf60` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00b0cf64"></a> `00b0cf64` | `80 00 00 b4` | cbz x0,0x00b0cf74 | `CONDITIONAL_JUMP`
<a id="insn-00b0cf68"></a> `00b0cf68` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b0cf6c"></a> `00b0cf6c` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b0cf70"></a> `00b0cf70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b0cf74"></a> `00b0cf74` | `7f 02 00 f9` | str xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b0cf78"></a> `00b0cf78` | `7f 22 00 39` | strb wzr,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b0cf7c"></a> `00b0cf7c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cf80"></a> `00b0cf80` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b0cf84"></a> `00b0cf84` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0cefc`](#insn-00b0cefc) 範囲 `[['00b0cefc', '00b0cf13']]`
  - `CONDITIONAL_JUMP` [`00b0cf10`](#insn-00b0cf10) → [`00b0cf28`](#insn-00b0cf28)
  - `FALL_THROUGH` [`00b0cf10`](#insn-00b0cf10) → [`00b0cf14`](#insn-00b0cf14)
- ブロック [`00b0cf14`](#insn-00b0cf14) 範囲 `[['00b0cf14', '00b0cf27']]`
  - `FALL_THROUGH` [`00b0cf24`](#insn-00b0cf24) → [`00b0cf28`](#insn-00b0cf28)
- ブロック [`00b0cf28`](#insn-00b0cf28) 範囲 `[['00b0cf28', '00b0cf2b']]`
  - `FALL_THROUGH` [`00b0cf28`](#insn-00b0cf28) → [`00b0cf2c`](#insn-00b0cf2c)
- ブロック [`00b0cf2c`](#insn-00b0cf2c) 範囲 `[['00b0cf2c', '00b0cf2f']]`
  - `CONDITIONAL_JUMP` [`00b0cf2c`](#insn-00b0cf2c) → [`00b0cf54`](#insn-00b0cf54)
  - `FALL_THROUGH` [`00b0cf2c`](#insn-00b0cf2c) → [`00b0cf30`](#insn-00b0cf30)
- ブロック [`00b0cf30`](#insn-00b0cf30) 範囲 `[['00b0cf30', '00b0cf37']]`
  - `CONDITIONAL_JUMP` [`00b0cf34`](#insn-00b0cf34) → [`00b0cf4c`](#insn-00b0cf4c)
  - `FALL_THROUGH` [`00b0cf34`](#insn-00b0cf34) → [`00b0cf38`](#insn-00b0cf38)
- ブロック [`00b0cf38`](#insn-00b0cf38) 範囲 `[['00b0cf38', '00b0cf4b']]`
  - `UNCONDITIONAL_JUMP` [`00b0cf48`](#insn-00b0cf48) → [`00b0cf54`](#insn-00b0cf54)
- ブロック [`00b0cf4c`](#insn-00b0cf4c) 範囲 `[['00b0cf4c', '00b0cf53']]`
  - `FALL_THROUGH` [`00b0cf50`](#insn-00b0cf50) → [`00b0cf54`](#insn-00b0cf54)
- ブロック [`00b0cf54`](#insn-00b0cf54) 範囲 `[['00b0cf54', '00b0cf5f']]`
  - `CONDITIONAL_JUMP` [`00b0cf5c`](#insn-00b0cf5c) → [`00b0cf74`](#insn-00b0cf74)
  - `FALL_THROUGH` [`00b0cf5c`](#insn-00b0cf5c) → [`00b0cf60`](#insn-00b0cf60)
- ブロック [`00b0cf60`](#insn-00b0cf60) 範囲 `[['00b0cf60', '00b0cf67']]`
  - `CONDITIONAL_JUMP` [`00b0cf64`](#insn-00b0cf64) → [`00b0cf74`](#insn-00b0cf74)
  - `FALL_THROUGH` [`00b0cf64`](#insn-00b0cf64) → [`00b0cf68`](#insn-00b0cf68)
- ブロック [`00b0cf68`](#insn-00b0cf68) 範囲 `[['00b0cf68', '00b0cf73']]`
  - `FALL_THROUGH` [`00b0cf70`](#insn-00b0cf70) → [`00b0cf74`](#insn-00b0cf74)
- ブロック [`00b0cf74`](#insn-00b0cf74) 範囲 `[['00b0cf74', '00b0cf87']]`

## 命令位置別の参照

- [`00b0cefc`](#insn-00b0cefc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf00`](#insn-00b0cf00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf10`](#insn-00b0cf10) → [`00b0cf28`](#insn-00b0cf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf1c`](#insn-00b0cf1c) → [`00bdeb10`](../00bde/00bdeb10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdeb10` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf24`](#insn-00b0cf24) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf2c`](#insn-00b0cf2c) → [`00b0cf54`](#insn-00b0cf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf34`](#insn-00b0cf34) → [`00b0cf4c`](#insn-00b0cf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf48`](#insn-00b0cf48) → [`00b0cf54`](#insn-00b0cf54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf50`](#insn-00b0cf50) → [`00bdef40`](../00bde/00bdef40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdef40` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf5c`](#insn-00b0cf5c) → [`00b0cf74`](#insn-00b0cf74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf64`](#insn-00b0cf64) → [`00b0cf74`](#insn-00b0cf74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf7c`](#insn-00b0cf7c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0cefc`](#insn-00b0cefc)

~~~json
{
  "source": "00b0cefc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cf00`](#insn-00b0cf00)

~~~json
{
  "source": "00b0cf00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cf10`](#insn-00b0cf10)

~~~json
{
  "source": "00b0cf10",
  "target": "00b0cf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cf1c`](#insn-00b0cf1c)

~~~json
{
  "source": "00b0cf1c",
  "target": "00bdeb10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cf24`](#insn-00b0cf24)

~~~json
{
  "source": "00b0cf24",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cf2c`](#insn-00b0cf2c)

~~~json
{
  "source": "00b0cf2c",
  "target": "00b0cf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cf34`](#insn-00b0cf34)

~~~json
{
  "source": "00b0cf34",
  "target": "00b0cf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cf48`](#insn-00b0cf48)

~~~json
{
  "source": "00b0cf48",
  "target": "00b0cf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cf50`](#insn-00b0cf50)

~~~json
{
  "source": "00b0cf50",
  "target": "00bdef40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cf5c`](#insn-00b0cf5c)

~~~json
{
  "source": "00b0cf5c",
  "target": "00b0cf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cf64`](#insn-00b0cf64)

~~~json
{
  "source": "00b0cf64",
  "target": "00b0cf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cf7c`](#insn-00b0cf7c)

~~~json
{
  "source": "00b0cf7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
