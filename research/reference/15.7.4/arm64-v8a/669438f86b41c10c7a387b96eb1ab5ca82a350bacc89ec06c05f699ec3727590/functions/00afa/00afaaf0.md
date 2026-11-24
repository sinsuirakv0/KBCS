# 00afaaf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afaaac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afaaac.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-9702e620d9be57dd54ab8d4e0b8dae30)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5a874`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5a/00b5a874.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0060.md#compare-f4c00a5390f736dac3ca2bced2021a39)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaaf0",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b243bdf224aa79684abe88f9e57d5aed80b16893bac81fafe27940aa55849ccd",
  "source_text_sha256": "b243bdf224aa79684abe88f9e57d5aed80b16893bac81fafe27940aa55849ccd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaaf0",
        "00afabaf"
      ]
    ],
    "bytes_sha256": "11f31bc3ed09ab7a8cda224fc1bcd218ebcab455dd99c34d8dff8bf9adca1ede",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde970](../00bde/00bde970.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1385 bytes

~~~c

void _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
               (ulong *param_1,byte *param_2,ulong param_3,ulong param_4)

{
  ulong __n;
  byte bVar1;
  byte *pbVar2;
  void *__dest;
  ulong uVar3;
  
                    /* try { // try from 00afaaf4 to 00bfab13 has its CatchHandler @ 00afff84 */
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  bVar1 = *param_2;
  uVar3 = (ulong)(bVar1 >> 1);
  if ((bVar1 & 1) != 0) {
    uVar3 = *(ulong *)(param_2 + 8);
  }
  if (uVar3 < param_3) {
LAB_00afabac:
                    /* WARNING: Subroutine does not return */
    abort();
  }
  pbVar2 = *(byte **)(param_2 + 0x10);
  if ((bVar1 & 1) == 0) {
    pbVar2 = param_2 + 1;
  }
  __n = uVar3 - param_3;
  if (param_4 <= uVar3 - param_3) {
    __n = param_4;
  }
  if (0xffffffffffffffef < __n) goto LAB_00afabac;
  if (__n < 0x17) {
    __dest = (void *)((long)param_1 + 1);
    *(char *)param_1 = (char)((int)__n << 1);
    if (__n == 0) goto LAB_00afab94;
  }
  else {
    uVar3 = __n + 0x10 & 0xfffffffffffffff0;
    __dest = (void *)_Znwm(uVar3);
    param_1[1] = __n;
    param_1[2] = (ulong)__dest;
    *param_1 = uVar3 | 1;
  }
                    /* try { // try from 00afab8c to 00bfab93 has its CatchHandler @ 00aff560 */
  memcpy(__dest,pbVar2 + param_3,__n);
LAB_00afab94:
  *(undefined1 *)((long)__dest + __n) = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaaf0"></a> `00afaaf0` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00afaaf4"></a> `00afaaf4` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaaf8"></a> `00afaaf8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaafc"></a> `00afaafc` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afab00"></a> `00afab00` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00afab04"></a> `00afab04` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00afab08"></a> `00afab08` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afab0c"></a> `00afab0c` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00afab10"></a> `00afab10` | `29 04 40 f9` | ldr x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00afab14"></a> `00afab14` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afab18"></a> `00afab18` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afab1c"></a> `00afab1c` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00afab20"></a> `00afab20` | `29 01 02 eb` | subs x9,x9,x2 | `FALL_THROUGH`
<a id="insn-00afab24"></a> `00afab24` | `43 04 00 54` | b.cc 0x00afabac | `CONDITIONAL_JUMP`
<a id="insn-00afab28"></a> `00afab28` | `2a 08 40 f9` | ldr x10,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00afab2c"></a> `00afab2c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afab30"></a> `00afab30` | `57 15 81 9a` | csinc x23,x10,x1,ne | `FALL_THROUGH`
<a id="insn-00afab34"></a> `00afab34` | `3f 01 03 eb` | cmp x9,x3 | `FALL_THROUGH`
<a id="insn-00afab38"></a> `00afab38` | `35 31 83 9a` | csel x21,x9,x3,cc | `FALL_THROUGH`
<a id="insn-00afab3c"></a> `00afab3c` | `bf 42 00 b1` | cmn x21,#0x10 | `FALL_THROUGH`
<a id="insn-00afab40"></a> `00afab40` | `62 03 00 54` | b.cs 0x00afabac | `CONDITIONAL_JUMP`
<a id="insn-00afab44"></a> `00afab44` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00afab48"></a> `00afab48` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afab4c"></a> `00afab4c` | `bf 5e 00 f1` | cmp x21,#0x17 | `FALL_THROUGH`
<a id="insn-00afab50"></a> `00afab50` | `a2 00 00 54` | b.cs 0x00afab64 | `CONDITIONAL_JUMP`
<a id="insn-00afab54"></a> `00afab54` | `a8 7a 1f 53` | lsl w8,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00afab58"></a> `00afab58` | `68 16 00 38` | strb w8,[x19], #0x1 | `FALL_THROUGH`
<a id="insn-00afab5c"></a> `00afab5c` | `55 01 00 b5` | cbnz x21,0x00afab84 | `CONDITIONAL_JUMP`
<a id="insn-00afab60"></a> `00afab60` | `0d 00 00 14` | b 0x00afab94 | `UNCONDITIONAL_JUMP`
<a id="insn-00afab64"></a> `00afab64` | `a8 42 00 91` | add x8,x21,#0x10 | `FALL_THROUGH`
<a id="insn-00afab68"></a> `00afab68` | `16 ed 7c 92` | and x22,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00afab6c"></a> `00afab6c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00afab70"></a> `00afab70` | `34 81 03 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00afab74"></a> `00afab74` | `c8 02 40 b2` | orr x8,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00afab78"></a> `00afab78` | `75 82 00 a9` | stp x21,x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00afab7c"></a> `00afab7c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00afab80"></a> `00afab80` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afab84"></a> `00afab84` | `e1 02 14 8b` | add x1,x23,x20 | `FALL_THROUGH`
<a id="insn-00afab88"></a> `00afab88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afab8c"></a> `00afab8c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00afab90"></a> `00afab90` | `88 81 03 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00afab94"></a> `00afab94` | `7f 6a 35 38` | strb wzr,[x19, x21, LSL ] | `FALL_THROUGH`
<a id="insn-00afab98"></a> `00afab98` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afab9c"></a> `00afab9c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaba0"></a> `00afaba0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaba4"></a> `00afaba4` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00afaba8"></a> `00afaba8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afabac"></a> `00afabac` | `c5 8d 03 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaaf0`](#insn-00afaaf0) 範囲 `[['00afaaf0', '00afaaf3']]`
  - `FALL_THROUGH` [`00afaaf0`](#insn-00afaaf0) → [`00afaaf4`](#insn-00afaaf4)
- ブロック [`00afaaf4`](#insn-00afaaf4) 範囲 `[['00afaaf4', '00afab27']]`
  - `CONDITIONAL_JUMP` [`00afab24`](#insn-00afab24) → [`00afabac`](#insn-00afabac)
  - `FALL_THROUGH` [`00afab24`](#insn-00afab24) → [`00afab28`](#insn-00afab28)
- ブロック [`00afab28`](#insn-00afab28) 範囲 `[['00afab28', '00afab43']]`
  - `CONDITIONAL_JUMP` [`00afab40`](#insn-00afab40) → [`00afabac`](#insn-00afabac)
  - `FALL_THROUGH` [`00afab40`](#insn-00afab40) → [`00afab44`](#insn-00afab44)
- ブロック [`00afab44`](#insn-00afab44) 範囲 `[['00afab44', '00afab53']]`
  - `CONDITIONAL_JUMP` [`00afab50`](#insn-00afab50) → [`00afab64`](#insn-00afab64)
  - `FALL_THROUGH` [`00afab50`](#insn-00afab50) → [`00afab54`](#insn-00afab54)
- ブロック [`00afab54`](#insn-00afab54) 範囲 `[['00afab54', '00afab5f']]`
  - `CONDITIONAL_JUMP` [`00afab5c`](#insn-00afab5c) → [`00afab84`](#insn-00afab84)
  - `FALL_THROUGH` [`00afab5c`](#insn-00afab5c) → [`00afab60`](#insn-00afab60)
- ブロック [`00afab60`](#insn-00afab60) 範囲 `[['00afab60', '00afab63']]`
  - `UNCONDITIONAL_JUMP` [`00afab60`](#insn-00afab60) → [`00afab94`](#insn-00afab94)
- ブロック [`00afab64`](#insn-00afab64) 範囲 `[['00afab64', '00afab83']]`
  - `FALL_THROUGH` [`00afab80`](#insn-00afab80) → [`00afab84`](#insn-00afab84)
- ブロック [`00afab84`](#insn-00afab84) 範囲 `[['00afab84', '00afab8b']]`
  - `FALL_THROUGH` [`00afab88`](#insn-00afab88) → [`00afab8c`](#insn-00afab8c)
- ブロック [`00afab8c`](#insn-00afab8c) 範囲 `[['00afab8c', '00afab93']]`
  - `FALL_THROUGH` [`00afab90`](#insn-00afab90) → [`00afab94`](#insn-00afab94)
- ブロック [`00afab94`](#insn-00afab94) 範囲 `[['00afab94', '00afabab']]`
- ブロック [`00afabac`](#insn-00afabac) 範囲 `[['00afabac', '00afabaf']]`

## 命令位置別の参照

- [`00afaaf0`](#insn-00afaaf0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaaf4`](#insn-00afaaf4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaaf8`](#insn-00afaaf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaafc`](#insn-00afaafc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab24`](#insn-00afab24) → [`00afabac`](#insn-00afabac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab40`](#insn-00afab40) → [`00afabac`](#insn-00afabac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab50`](#insn-00afab50) → [`00afab64`](#insn-00afab64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab5c`](#insn-00afab5c) → [`00afab84`](#insn-00afab84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab60`](#insn-00afab60) → [`00afab94`](#insn-00afab94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab70`](#insn-00afab70) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00afab90`](#insn-00afab90) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00afab98`](#insn-00afab98) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afab9c`](#insn-00afab9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaba0`](#insn-00afaba0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afabac`](#insn-00afabac) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaaf0`](#insn-00afaaf0)

~~~json
{
  "source": "00afaaf0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaaf4`](#insn-00afaaf4)

~~~json
{
  "source": "00afaaf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaaf8`](#insn-00afaaf8)

~~~json
{
  "source": "00afaaf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaafc`](#insn-00afaafc)

~~~json
{
  "source": "00afaafc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab24`](#insn-00afab24)

~~~json
{
  "source": "00afab24",
  "target": "00afabac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab40`](#insn-00afab40)

~~~json
{
  "source": "00afab40",
  "target": "00afabac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab50`](#insn-00afab50)

~~~json
{
  "source": "00afab50",
  "target": "00afab64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab5c`](#insn-00afab5c)

~~~json
{
  "source": "00afab5c",
  "target": "00afab84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab60`](#insn-00afab60)

~~~json
{
  "source": "00afab60",
  "target": "00afab94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab70`](#insn-00afab70)

~~~json
{
  "source": "00afab70",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afab90`](#insn-00afab90)

~~~json
{
  "source": "00afab90",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afab98`](#insn-00afab98)

~~~json
{
  "source": "00afab98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afab9c`](#insn-00afab9c)

~~~json
{
  "source": "00afab9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaba0`](#insn-00afaba0)

~~~json
{
  "source": "00afaba0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afabac`](#insn-00afabac)

~~~json
{
  "source": "00afabac",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
