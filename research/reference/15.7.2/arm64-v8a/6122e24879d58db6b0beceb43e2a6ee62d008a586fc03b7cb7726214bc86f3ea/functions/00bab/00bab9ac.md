# 00bab9ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baba74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00baba74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-6d1b4067c2baddd6f0c37fa4ac009831)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bab9ac",
  "name": "_ZNKSt6__ndk17codecvtIwc9mbstate_tE10do_unshiftERS1_PcS4_RS4_",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d938319d40ff8ac555a4534e2d3d1a199eedd1fe340293917a61ca9d142d1fd6",
  "source_text_sha256": "d938319d40ff8ac555a4534e2d3d1a199eedd1fe340293917a61ca9d142d1fd6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bab9ac",
        "00baba73"
      ]
    ],
    "bytes_sha256": "99f813c7780322974ecc1cf3ffe347f9497edeb7463ea344bb558fb4a0d01674",
    "instruction_count": 50,
    "instruction_bytes": 200,
    "body_bytes": 200,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1480](../00be1/00be1480.md)
- [00be1a50](../00be1/00be1a50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1336 bytes

~~~c

undefined8
_ZNKSt6__ndk17codecvtIwc9mbstate_tE10do_unshiftERS1_PcS4_RS4_
          (long param_1,mbstate_t *param_2,long param_3,long param_4,long *param_5)

{
  char cVar1;
  __locale_t __dataset;
  size_t sVar2;
  undefined8 uVar3;
  ulong uVar4;
  char *pcVar5;
  char *pcVar6;
  char acStack_3c [4];
  __locale_t local_38;
  
  *param_5 = param_3;
  __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
  local_38 = __dataset;
  sVar2 = wcrtomb(acStack_3c,L'\0',param_2);
  if (__dataset != (__locale_t)0x0) {
                    /* try { // try from 00baba00 to 00caba17 has its CatchHandler @ 00babc6c */
    uselocale(__dataset);
  }
  if (sVar2 + 1 < 2) {
    uVar3 = 2;
  }
  else {
    uVar4 = sVar2 - 1;
    if ((ulong)(param_4 - *param_5) < uVar4) {
      uVar3 = 1;
    }
    else {
      if (uVar4 != 0) {
        pcVar5 = acStack_3c;
        do {
          pcVar6 = (char *)*param_5;
          cVar1 = *pcVar5;
                    /* try { // try from 00baba44 to 00caba63 has its CatchHandler @ 00babbfc */
          uVar4 = uVar4 - 1;
          *param_5 = (long)(pcVar6 + 1);
          *pcVar6 = cVar1;
          pcVar5 = pcVar5 + 1;
        } while (uVar4 != 0);
      }
      uVar3 = 0;
    }
  }
                    /* try { // try from 00baba64 to 00cabb57 has its CatchHandler @ 00bab67c */
  return uVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bab9ac"></a> `00bab9ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bab9b0"></a> `00bab9b0` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bab9b4"></a> `00bab9b4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab9b8"></a> `00bab9b8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab9bc"></a> `00bab9bc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bab9c0"></a> `00bab9c0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bab9c4"></a> `00bab9c4` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00bab9c8"></a> `00bab9c8` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00bab9cc"></a> `00bab9cc` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bab9d0"></a> `00bab9d0` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bab9d4"></a> `00bab9d4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bab9d8"></a> `00bab9d8` | `aa d6 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00bab9dc"></a> `00bab9dc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bab9e0"></a> `00bab9e0` | `e0 07 00 f9` | str x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bab9e4"></a> `00bab9e4` | `e0 13 00 91` | add x0,sp,#0x4 | `FALL_THROUGH`
<a id="insn-00bab9e8"></a> `00bab9e8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bab9ec"></a> `00bab9ec` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bab9f0"></a> `00bab9f0` | `18 d8 00 94` | bl 0x00be1a50 | `UNCONDITIONAL_CALL`
<a id="insn-00bab9f4"></a> `00bab9f4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bab9f8"></a> `00bab9f8` | `76 00 00 b4` | cbz x22,0x00baba04 | `CONDITIONAL_JUMP`
<a id="insn-00bab9fc"></a> `00bab9fc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00baba00"></a> `00baba00` | `a0 d6 00 94` | bl 0x00be1480 | `UNCONDITIONAL_CALL`
<a id="insn-00baba04"></a> `00baba04` | `a8 06 00 91` | add x8,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00baba08"></a> `00baba08` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00baba0c"></a> `00baba0c` | `62 00 00 54` | b.cs 0x00baba18 | `CONDITIONAL_JUMP`
<a id="insn-00baba10"></a> `00baba10` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00baba14"></a> `00baba14` | `12 00 00 14` | b 0x00baba5c | `UNCONDITIONAL_JUMP`
<a id="insn-00baba18"></a> `00baba18` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00baba1c"></a> `00baba1c` | `a8 06 00 d1` | sub x8,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00baba20"></a> `00baba20` | `89 02 09 cb` | sub x9,x20,x9 | `FALL_THROUGH`
<a id="insn-00baba24"></a> `00baba24` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00baba28"></a> `00baba28` | `69 00 00 54` | b.ls 0x00baba34 | `CONDITIONAL_JUMP`
<a id="insn-00baba2c"></a> `00baba2c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00baba30"></a> `00baba30` | `0b 00 00 14` | b 0x00baba5c | `UNCONDITIONAL_JUMP`
<a id="insn-00baba34"></a> `00baba34` | `28 01 00 b4` | cbz x8,0x00baba58 | `CONDITIONAL_JUMP`
<a id="insn-00baba38"></a> `00baba38` | `e9 13 00 91` | add x9,sp,#0x4 | `FALL_THROUGH`
<a id="insn-00baba3c"></a> `00baba3c` | `6a 02 40 f9` | ldr x10,[x19] | `FALL_THROUGH`
<a id="insn-00baba40"></a> `00baba40` | `2b 15 40 38` | ldrb w11,[x9], #0x1 | `FALL_THROUGH`
<a id="insn-00baba44"></a> `00baba44` | `08 05 00 f1` | subs x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baba48"></a> `00baba48` | `4c 05 00 91` | add x12,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00baba4c"></a> `00baba4c` | `6c 02 00 f9` | str x12,[x19] | `FALL_THROUGH`
<a id="insn-00baba50"></a> `00baba50` | `4b 01 00 39` | strb w11,[x10] | `FALL_THROUGH`
<a id="insn-00baba54"></a> `00baba54` | `41 ff ff 54` | b.ne 0x00baba3c | `CONDITIONAL_JUMP`
<a id="insn-00baba58"></a> `00baba58` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00baba5c"></a> `00baba5c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baba60"></a> `00baba60` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baba64"></a> `00baba64` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baba68"></a> `00baba68` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00baba6c"></a> `00baba6c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baba70"></a> `00baba70` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bab9ac`](#insn-00bab9ac) 範囲 `[['00bab9ac', '00bab9fb']]`
  - `CONDITIONAL_JUMP` [`00bab9f8`](#insn-00bab9f8) → [`00baba04`](#insn-00baba04)
  - `FALL_THROUGH` [`00bab9f8`](#insn-00bab9f8) → [`00bab9fc`](#insn-00bab9fc)
- ブロック [`00bab9fc`](#insn-00bab9fc) 範囲 `[['00bab9fc', '00bab9ff']]`
  - `FALL_THROUGH` [`00bab9fc`](#insn-00bab9fc) → [`00baba00`](#insn-00baba00)
- ブロック [`00baba00`](#insn-00baba00) 範囲 `[['00baba00', '00baba03']]`
  - `FALL_THROUGH` [`00baba00`](#insn-00baba00) → [`00baba04`](#insn-00baba04)
- ブロック [`00baba04`](#insn-00baba04) 範囲 `[['00baba04', '00baba0f']]`
  - `CONDITIONAL_JUMP` [`00baba0c`](#insn-00baba0c) → [`00baba18`](#insn-00baba18)
  - `FALL_THROUGH` [`00baba0c`](#insn-00baba0c) → [`00baba10`](#insn-00baba10)
- ブロック [`00baba10`](#insn-00baba10) 範囲 `[['00baba10', '00baba17']]`
  - `UNCONDITIONAL_JUMP` [`00baba14`](#insn-00baba14) → [`00baba5c`](#insn-00baba5c)
- ブロック [`00baba18`](#insn-00baba18) 範囲 `[['00baba18', '00baba2b']]`
  - `CONDITIONAL_JUMP` [`00baba28`](#insn-00baba28) → [`00baba34`](#insn-00baba34)
  - `FALL_THROUGH` [`00baba28`](#insn-00baba28) → [`00baba2c`](#insn-00baba2c)
- ブロック [`00baba2c`](#insn-00baba2c) 範囲 `[['00baba2c', '00baba33']]`
  - `UNCONDITIONAL_JUMP` [`00baba30`](#insn-00baba30) → [`00baba5c`](#insn-00baba5c)
- ブロック [`00baba34`](#insn-00baba34) 範囲 `[['00baba34', '00baba37']]`
  - `CONDITIONAL_JUMP` [`00baba34`](#insn-00baba34) → [`00baba58`](#insn-00baba58)
  - `FALL_THROUGH` [`00baba34`](#insn-00baba34) → [`00baba38`](#insn-00baba38)
- ブロック [`00baba38`](#insn-00baba38) 範囲 `[['00baba38', '00baba3b']]`
  - `FALL_THROUGH` [`00baba38`](#insn-00baba38) → [`00baba3c`](#insn-00baba3c)
- ブロック [`00baba3c`](#insn-00baba3c) 範囲 `[['00baba3c', '00baba43']]`
  - `FALL_THROUGH` [`00baba40`](#insn-00baba40) → [`00baba44`](#insn-00baba44)
- ブロック [`00baba44`](#insn-00baba44) 範囲 `[['00baba44', '00baba57']]`
  - `CONDITIONAL_JUMP` [`00baba54`](#insn-00baba54) → [`00baba3c`](#insn-00baba3c)
  - `FALL_THROUGH` [`00baba54`](#insn-00baba54) → [`00baba58`](#insn-00baba58)
- ブロック [`00baba58`](#insn-00baba58) 範囲 `[['00baba58', '00baba5b']]`
  - `FALL_THROUGH` [`00baba58`](#insn-00baba58) → [`00baba5c`](#insn-00baba5c)
- ブロック [`00baba5c`](#insn-00baba5c) 範囲 `[['00baba5c', '00baba63']]`
  - `FALL_THROUGH` [`00baba60`](#insn-00baba60) → [`00baba64`](#insn-00baba64)
- ブロック [`00baba64`](#insn-00baba64) 範囲 `[['00baba64', '00baba73']]`

## 命令位置別の参照

- [`00bab9b4`](#insn-00bab9b4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab9b8`](#insn-00bab9b8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab9bc`](#insn-00bab9bc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab9d8`](#insn-00bab9d8) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00bab9e0`](#insn-00bab9e0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab9f0`](#insn-00bab9f0) → [`00be1a50`](../00be1/00be1a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a50` · 推定シンボル `None` · 推定型 `None`
- [`00bab9f8`](#insn-00bab9f8) → [`00baba04`](#insn-00baba04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba00`](#insn-00baba00) → [`00be1480`](../00be1/00be1480.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1480` · 推定シンボル `None` · 推定型 `None`
- [`00baba0c`](#insn-00baba0c) → [`00baba18`](#insn-00baba18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba14`](#insn-00baba14) → [`00baba5c`](#insn-00baba5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba28`](#insn-00baba28) → [`00baba34`](#insn-00baba34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba30`](#insn-00baba30) → [`00baba5c`](#insn-00baba5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba34`](#insn-00baba34) → [`00baba58`](#insn-00baba58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba54`](#insn-00baba54) → [`00baba3c`](#insn-00baba3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba5c`](#insn-00baba5c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba60`](#insn-00baba60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baba64`](#insn-00baba64) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bab9b4`](#insn-00bab9b4)

~~~json
{
  "source": "00bab9b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab9b8`](#insn-00bab9b8)

~~~json
{
  "source": "00bab9b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab9bc`](#insn-00bab9bc)

~~~json
{
  "source": "00bab9bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab9d8`](#insn-00bab9d8)

~~~json
{
  "source": "00bab9d8",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab9e0`](#insn-00bab9e0)

~~~json
{
  "source": "00bab9e0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab9f0`](#insn-00bab9f0)

~~~json
{
  "source": "00bab9f0",
  "target": "00be1a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab9f8`](#insn-00bab9f8)

~~~json
{
  "source": "00bab9f8",
  "target": "00baba04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba00`](#insn-00baba00)

~~~json
{
  "source": "00baba00",
  "target": "00be1480",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baba0c`](#insn-00baba0c)

~~~json
{
  "source": "00baba0c",
  "target": "00baba18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba14`](#insn-00baba14)

~~~json
{
  "source": "00baba14",
  "target": "00baba5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba28`](#insn-00baba28)

~~~json
{
  "source": "00baba28",
  "target": "00baba34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba30`](#insn-00baba30)

~~~json
{
  "source": "00baba30",
  "target": "00baba5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba34`](#insn-00baba34)

~~~json
{
  "source": "00baba34",
  "target": "00baba58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba54`](#insn-00baba54)

~~~json
{
  "source": "00baba54",
  "target": "00baba3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba5c`](#insn-00baba5c)

~~~json
{
  "source": "00baba5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba60`](#insn-00baba60)

~~~json
{
  "source": "00baba60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baba64`](#insn-00baba64)

~~~json
{
  "source": "00baba64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
