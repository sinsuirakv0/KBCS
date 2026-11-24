# 00bddea4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6e9a4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6e/00b6e9a4.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-42871fad07910403ae2070d8330c71ac)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bde2cc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bde/00bde2cc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0010.md#compare-c4ac328da3b4b78e9694c0458b16d33a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddea4",
  "name": "_ZNK8firebase4auth4User3uidEv",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b0e5cafbb43971e15a05b0d320bcc698eaa2c0f9c29bb873d1155fcb8f9e77f3",
  "source_text_sha256": "b0e5cafbb43971e15a05b0d320bcc698eaa2c0f9c29bb873d1155fcb8f9e77f3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddea4",
        "00bddf47"
      ]
    ],
    "bytes_sha256": "f5e15689e9b9c3140042e56c9d09d855aee8893397f0166f05195b4d05791bb9",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5af90](../00c5a/00c5af90.md)
- [00c5b1c0](../00c5b/00c5b1c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 787 bytes

~~~c

void _ZNK8firebase4auth4User3uidEv(undefined8 *param_1,long param_2)

{
  undefined8 uVar1;
  ulong uVar2;
  undefined8 *puVar3;
  long lVar4;
  
  puVar3 = *(undefined8 **)(param_2 + 0x98);
  if ((puVar3 == (undefined8 *)0x0) || (lVar4 = puVar3[0x40], lVar4 == 0)) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
              (param_1,&DAT_002a630e);
    return;
  }
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*puVar3);
  lVar4 = FUN_004977f4(uVar1,lVar4,DAT_011269c0);
  uVar2 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
  if ((lVar4 != 0) && ((uVar2 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar1,lVar4);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddea4"></a> `00bddea4` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bddea8"></a> `00bddea8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddeac"></a> `00bddeac` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddeb0"></a> `00bddeb0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bddeb4"></a> `00bddeb4` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bddeb8"></a> `00bddeb8` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bddebc"></a> `00bddebc` | `c9 02 00 b4` | cbz x9,0x00bddf14 | `CONDITIONAL_JUMP`
<a id="insn-00bddec0"></a> `00bddec0` | `35 01 41 f9` | ldr x21,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00bddec4"></a> `00bddec4` | `95 02 00 b4` | cbz x21,0x00bddf14 | `CONDITIONAL_JUMP`
<a id="insn-00bddec8"></a> `00bddec8` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bddecc"></a> `00bddecc` | `6d f3 01 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdded0"></a> `00bdded0` | `48 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdded4"></a> `00bdded4` | `02 e1 44 f9` | ldr x2,[x8, #0x9c0] | `FALL_THROUGH`
<a id="insn-00bdded8"></a> `00bdded8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bddedc"></a> `00bddedc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bddee0"></a> `00bddee0` | `45 e6 e2 97` | bl 0x004977f4 | `UNCONDITIONAL_CALL`
<a id="insn-00bddee4"></a> `00bddee4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bddee8"></a> `00bddee8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bddeec"></a> `00bddeec` | `1d f3 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bddef0"></a> `00bddef0` | `15 02 00 b4` | cbz x21,0x00bddf30 | `CONDITIONAL_JUMP`
<a id="insn-00bddef4"></a> `00bddef4` | `e0 01 00 37` | tbnz w0,#0x0,0x00bddf30 | `CONDITIONAL_JUMP`
<a id="insn-00bddef8"></a> `00bddef8` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bddefc"></a> `00bddefc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bddf00"></a> `00bddf00` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddf04"></a> `00bddf04` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddf08"></a> `00bddf08` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bddf0c"></a> `00bddf0c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bddf10"></a> `00bddf10` | `20 f4 01 14` | b 0x00c5af90 | `CALL_TERMINATOR`
<a id="insn-00bddf14"></a> `00bddf14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddf18"></a> `00bddf18` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddf1c"></a> `00bddf1c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddf20"></a> `00bddf20` | `41 b6 ff b0` | adrp x1,0x2a6000 | `FALL_THROUGH`
<a id="insn-00bddf24"></a> `00bddf24` | `21 38 0c 91` | add x1,x1,#0x30e | `FALL_THROUGH`
<a id="insn-00bddf28"></a> `00bddf28` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bddf2c"></a> `00bddf2c` | `a5 f4 01 14` | b 0x00c5b1c0 | `CALL_TERMINATOR`
<a id="insn-00bddf30"></a> `00bddf30` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bddf34"></a> `00bddf34` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bddf38"></a> `00bddf38` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddf3c"></a> `00bddf3c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddf40"></a> `00bddf40` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bddf44"></a> `00bddf44` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddea4`](#insn-00bddea4) 範囲 `[['00bddea4', '00bddebf']]`
  - `CONDITIONAL_JUMP` [`00bddebc`](#insn-00bddebc) → [`00bddf14`](#insn-00bddf14)
  - `FALL_THROUGH` [`00bddebc`](#insn-00bddebc) → [`00bddec0`](#insn-00bddec0)
- ブロック [`00bddec0`](#insn-00bddec0) 範囲 `[['00bddec0', '00bddec7']]`
  - `CONDITIONAL_JUMP` [`00bddec4`](#insn-00bddec4) → [`00bddf14`](#insn-00bddf14)
  - `FALL_THROUGH` [`00bddec4`](#insn-00bddec4) → [`00bddec8`](#insn-00bddec8)
- ブロック [`00bddec8`](#insn-00bddec8) 範囲 `[['00bddec8', '00bddef3']]`
  - `CONDITIONAL_JUMP` [`00bddef0`](#insn-00bddef0) → [`00bddf30`](#insn-00bddf30)
  - `FALL_THROUGH` [`00bddef0`](#insn-00bddef0) → [`00bddef4`](#insn-00bddef4)
- ブロック [`00bddef4`](#insn-00bddef4) 範囲 `[['00bddef4', '00bddef7']]`
  - `CONDITIONAL_JUMP` [`00bddef4`](#insn-00bddef4) → [`00bddf30`](#insn-00bddf30)
  - `FALL_THROUGH` [`00bddef4`](#insn-00bddef4) → [`00bddef8`](#insn-00bddef8)
- ブロック [`00bddef8`](#insn-00bddef8) 範囲 `[['00bddef8', '00bddf13']]`
- ブロック [`00bddf14`](#insn-00bddf14) 範囲 `[['00bddf14', '00bddf2f']]`
- ブロック [`00bddf30`](#insn-00bddf30) 範囲 `[['00bddf30', '00bddf47']]`

## 命令位置別の参照

- [`00bddea4`](#insn-00bddea4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddea8`](#insn-00bddea8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddeac`](#insn-00bddeac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddebc`](#insn-00bddebc) → [`00bddf14`](#insn-00bddf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddec4`](#insn-00bddec4) → [`00bddf14`](#insn-00bddf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddecc`](#insn-00bddecc) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bdded4`](#insn-00bdded4) → `011269c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddee0`](#insn-00bddee0) → [`004977f4`](../00497/004977f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004977f4` · 推定シンボル `None` · 推定型 `None`
- [`00bddeec`](#insn-00bddeec) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bddef0`](#insn-00bddef0) → [`00bddf30`](#insn-00bddf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddef4`](#insn-00bddef4) → [`00bddf30`](#insn-00bddf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf00`](#insn-00bddf00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf04`](#insn-00bddf04) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf10`](#insn-00bddf10) → [`00c5af90`](../00c5a/00c5af90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af90` · 推定シンボル `None` · 推定型 `None`
- [`00bddf18`](#insn-00bddf18) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf1c`](#insn-00bddf1c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf24`](#insn-00bddf24) → `002a630e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bddf2c`](#insn-00bddf2c) → [`00c5b1c0`](../00c5b/00c5b1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bddf38`](#insn-00bddf38) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf3c`](#insn-00bddf3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddea4`](#insn-00bddea4)

~~~json
{
  "source": "00bddea4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddea8`](#insn-00bddea8)

~~~json
{
  "source": "00bddea8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddeac`](#insn-00bddeac)

~~~json
{
  "source": "00bddeac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddebc`](#insn-00bddebc)

~~~json
{
  "source": "00bddebc",
  "target": "00bddf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddec4`](#insn-00bddec4)

~~~json
{
  "source": "00bddec4",
  "target": "00bddf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddecc`](#insn-00bddecc)

~~~json
{
  "source": "00bddecc",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdded4`](#insn-00bdded4)

~~~json
{
  "source": "00bdded4",
  "target": "011269c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddee0`](#insn-00bddee0)

~~~json
{
  "source": "00bddee0",
  "target": "004977f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddeec`](#insn-00bddeec)

~~~json
{
  "source": "00bddeec",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddef0`](#insn-00bddef0)

~~~json
{
  "source": "00bddef0",
  "target": "00bddf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddef4`](#insn-00bddef4)

~~~json
{
  "source": "00bddef4",
  "target": "00bddf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf00`](#insn-00bddf00)

~~~json
{
  "source": "00bddf00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf04`](#insn-00bddf04)

~~~json
{
  "source": "00bddf04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf10`](#insn-00bddf10)

~~~json
{
  "source": "00bddf10",
  "target": "00c5af90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddf18`](#insn-00bddf18)

~~~json
{
  "source": "00bddf18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf1c`](#insn-00bddf1c)

~~~json
{
  "source": "00bddf1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf24`](#insn-00bddf24)

~~~json
{
  "source": "00bddf24",
  "target": "002a630e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a630e",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a630e",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bddf2c`](#insn-00bddf2c)

~~~json
{
  "source": "00bddf2c",
  "target": "00c5b1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddf38`](#insn-00bddf38)

~~~json
{
  "source": "00bddf38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf3c`](#insn-00bddf3c)

~~~json
{
  "source": "00bddf3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
