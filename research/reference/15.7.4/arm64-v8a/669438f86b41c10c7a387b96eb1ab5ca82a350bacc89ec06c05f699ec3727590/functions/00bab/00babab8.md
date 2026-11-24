# 00babab8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baba74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00baba74.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-c52527a8b393cabfcecc8e421183ffe2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c28500`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28500.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0075.md#compare-c77abb9e6941d36f6a056a87b49e2afb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babab8",
  "name": "_ZNKSt6__ndk17codecvtIwc9mbstate_tE10do_unshiftERS1_PcS4_RS4_",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "38abbb1846e44cfddf0788602584ee7b5eb4b9c71323d15148a4041ef18792ed",
  "source_text_sha256": "38abbb1846e44cfddf0788602584ee7b5eb4b9c71323d15148a4041ef18792ed",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00babab8",
        "00babb7f"
      ]
    ],
    "bytes_sha256": "dd7b1efeda4eca3f6e7cc0396dac6ea47bfab255b675f964eb01160305b26fa4",
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

- [00be1580](../00be1/00be1580.md)
- [00be1b50](../00be1/00be1b50.md)

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
                    /* try { // try from 00babb0c to 00cabb23 has its CatchHandler @ 00babd78 */
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
                    /* try { // try from 00babb50 to 00cabb6f has its CatchHandler @ 00babd08 */
          uVar4 = uVar4 - 1;
          *param_5 = (long)(pcVar6 + 1);
          *pcVar6 = cVar1;
          pcVar5 = pcVar5 + 1;
        } while (uVar4 != 0);
      }
      uVar3 = 0;
    }
  }
                    /* try { // try from 00babb70 to 00cabc63 has its CatchHandler @ 00bab788 */
  return uVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00babab8"></a> `00babab8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bababc"></a> `00bababc` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00babac0"></a> `00babac0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babac4"></a> `00babac4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babac8"></a> `00babac8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00babacc"></a> `00babacc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00babad0"></a> `00babad0` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00babad4"></a> `00babad4` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00babad8"></a> `00babad8` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00babadc"></a> `00babadc` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00babae0"></a> `00babae0` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00babae4"></a> `00babae4` | `a7 d6 00 94` | bl 0x00be1580 | `UNCONDITIONAL_CALL`
<a id="insn-00babae8"></a> `00babae8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00babaec"></a> `00babaec` | `e0 07 00 f9` | str x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00babaf0"></a> `00babaf0` | `e0 13 00 91` | add x0,sp,#0x4 | `FALL_THROUGH`
<a id="insn-00babaf4"></a> `00babaf4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00babaf8"></a> `00babaf8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00babafc"></a> `00babafc` | `15 d8 00 94` | bl 0x00be1b50 | `UNCONDITIONAL_CALL`
<a id="insn-00babb00"></a> `00babb00` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00babb04"></a> `00babb04` | `76 00 00 b4` | cbz x22,0x00babb10 | `CONDITIONAL_JUMP`
<a id="insn-00babb08"></a> `00babb08` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00babb0c"></a> `00babb0c` | `9d d6 00 94` | bl 0x00be1580 | `UNCONDITIONAL_CALL`
<a id="insn-00babb10"></a> `00babb10` | `a8 06 00 91` | add x8,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00babb14"></a> `00babb14` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00babb18"></a> `00babb18` | `62 00 00 54` | b.cs 0x00babb24 | `CONDITIONAL_JUMP`
<a id="insn-00babb1c"></a> `00babb1c` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00babb20"></a> `00babb20` | `12 00 00 14` | b 0x00babb68 | `UNCONDITIONAL_JUMP`
<a id="insn-00babb24"></a> `00babb24` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00babb28"></a> `00babb28` | `a8 06 00 d1` | sub x8,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00babb2c"></a> `00babb2c` | `89 02 09 cb` | sub x9,x20,x9 | `FALL_THROUGH`
<a id="insn-00babb30"></a> `00babb30` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00babb34"></a> `00babb34` | `69 00 00 54` | b.ls 0x00babb40 | `CONDITIONAL_JUMP`
<a id="insn-00babb38"></a> `00babb38` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00babb3c"></a> `00babb3c` | `0b 00 00 14` | b 0x00babb68 | `UNCONDITIONAL_JUMP`
<a id="insn-00babb40"></a> `00babb40` | `28 01 00 b4` | cbz x8,0x00babb64 | `CONDITIONAL_JUMP`
<a id="insn-00babb44"></a> `00babb44` | `e9 13 00 91` | add x9,sp,#0x4 | `FALL_THROUGH`
<a id="insn-00babb48"></a> `00babb48` | `6a 02 40 f9` | ldr x10,[x19] | `FALL_THROUGH`
<a id="insn-00babb4c"></a> `00babb4c` | `2b 15 40 38` | ldrb w11,[x9], #0x1 | `FALL_THROUGH`
<a id="insn-00babb50"></a> `00babb50` | `08 05 00 f1` | subs x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00babb54"></a> `00babb54` | `4c 05 00 91` | add x12,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00babb58"></a> `00babb58` | `6c 02 00 f9` | str x12,[x19] | `FALL_THROUGH`
<a id="insn-00babb5c"></a> `00babb5c` | `4b 01 00 39` | strb w11,[x10] | `FALL_THROUGH`
<a id="insn-00babb60"></a> `00babb60` | `41 ff ff 54` | b.ne 0x00babb48 | `CONDITIONAL_JUMP`
<a id="insn-00babb64"></a> `00babb64` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00babb68"></a> `00babb68` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00babb6c"></a> `00babb6c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babb70"></a> `00babb70` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babb74"></a> `00babb74` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00babb78"></a> `00babb78` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00babb7c"></a> `00babb7c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00babab8`](#insn-00babab8) 範囲 `[['00babab8', '00babb07']]`
  - `CONDITIONAL_JUMP` [`00babb04`](#insn-00babb04) → [`00babb10`](#insn-00babb10)
  - `FALL_THROUGH` [`00babb04`](#insn-00babb04) → [`00babb08`](#insn-00babb08)
- ブロック [`00babb08`](#insn-00babb08) 範囲 `[['00babb08', '00babb0b']]`
  - `FALL_THROUGH` [`00babb08`](#insn-00babb08) → [`00babb0c`](#insn-00babb0c)
- ブロック [`00babb0c`](#insn-00babb0c) 範囲 `[['00babb0c', '00babb0f']]`
  - `FALL_THROUGH` [`00babb0c`](#insn-00babb0c) → [`00babb10`](#insn-00babb10)
- ブロック [`00babb10`](#insn-00babb10) 範囲 `[['00babb10', '00babb1b']]`
  - `CONDITIONAL_JUMP` [`00babb18`](#insn-00babb18) → [`00babb24`](#insn-00babb24)
  - `FALL_THROUGH` [`00babb18`](#insn-00babb18) → [`00babb1c`](#insn-00babb1c)
- ブロック [`00babb1c`](#insn-00babb1c) 範囲 `[['00babb1c', '00babb23']]`
  - `UNCONDITIONAL_JUMP` [`00babb20`](#insn-00babb20) → [`00babb68`](#insn-00babb68)
- ブロック [`00babb24`](#insn-00babb24) 範囲 `[['00babb24', '00babb37']]`
  - `CONDITIONAL_JUMP` [`00babb34`](#insn-00babb34) → [`00babb40`](#insn-00babb40)
  - `FALL_THROUGH` [`00babb34`](#insn-00babb34) → [`00babb38`](#insn-00babb38)
- ブロック [`00babb38`](#insn-00babb38) 範囲 `[['00babb38', '00babb3f']]`
  - `UNCONDITIONAL_JUMP` [`00babb3c`](#insn-00babb3c) → [`00babb68`](#insn-00babb68)
- ブロック [`00babb40`](#insn-00babb40) 範囲 `[['00babb40', '00babb43']]`
  - `CONDITIONAL_JUMP` [`00babb40`](#insn-00babb40) → [`00babb64`](#insn-00babb64)
  - `FALL_THROUGH` [`00babb40`](#insn-00babb40) → [`00babb44`](#insn-00babb44)
- ブロック [`00babb44`](#insn-00babb44) 範囲 `[['00babb44', '00babb47']]`
  - `FALL_THROUGH` [`00babb44`](#insn-00babb44) → [`00babb48`](#insn-00babb48)
- ブロック [`00babb48`](#insn-00babb48) 範囲 `[['00babb48', '00babb4f']]`
  - `FALL_THROUGH` [`00babb4c`](#insn-00babb4c) → [`00babb50`](#insn-00babb50)
- ブロック [`00babb50`](#insn-00babb50) 範囲 `[['00babb50', '00babb63']]`
  - `CONDITIONAL_JUMP` [`00babb60`](#insn-00babb60) → [`00babb48`](#insn-00babb48)
  - `FALL_THROUGH` [`00babb60`](#insn-00babb60) → [`00babb64`](#insn-00babb64)
- ブロック [`00babb64`](#insn-00babb64) 範囲 `[['00babb64', '00babb67']]`
  - `FALL_THROUGH` [`00babb64`](#insn-00babb64) → [`00babb68`](#insn-00babb68)
- ブロック [`00babb68`](#insn-00babb68) 範囲 `[['00babb68', '00babb6f']]`
  - `FALL_THROUGH` [`00babb6c`](#insn-00babb6c) → [`00babb70`](#insn-00babb70)
- ブロック [`00babb70`](#insn-00babb70) 範囲 `[['00babb70', '00babb7f']]`

## 命令位置別の参照

- [`00babac0`](#insn-00babac0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babac4`](#insn-00babac4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babac8`](#insn-00babac8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babae4`](#insn-00babae4) → [`00be1580`](../00be1/00be1580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1580` · 推定シンボル `None` · 推定型 `None`
- [`00babaec`](#insn-00babaec) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babafc`](#insn-00babafc) → [`00be1b50`](../00be1/00be1b50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1b50` · 推定シンボル `None` · 推定型 `None`
- [`00babb04`](#insn-00babb04) → [`00babb10`](#insn-00babb10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb0c`](#insn-00babb0c) → [`00be1580`](../00be1/00be1580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1580` · 推定シンボル `None` · 推定型 `None`
- [`00babb18`](#insn-00babb18) → [`00babb24`](#insn-00babb24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb20`](#insn-00babb20) → [`00babb68`](#insn-00babb68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb34`](#insn-00babb34) → [`00babb40`](#insn-00babb40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb3c`](#insn-00babb3c) → [`00babb68`](#insn-00babb68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb40`](#insn-00babb40) → [`00babb64`](#insn-00babb64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb60`](#insn-00babb60) → [`00babb48`](#insn-00babb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb68`](#insn-00babb68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb6c`](#insn-00babb6c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb70`](#insn-00babb70) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00babac0`](#insn-00babac0)

~~~json
{
  "source": "00babac0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babac4`](#insn-00babac4)

~~~json
{
  "source": "00babac4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babac8`](#insn-00babac8)

~~~json
{
  "source": "00babac8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babae4`](#insn-00babae4)

~~~json
{
  "source": "00babae4",
  "target": "00be1580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babaec`](#insn-00babaec)

~~~json
{
  "source": "00babaec",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babafc`](#insn-00babafc)

~~~json
{
  "source": "00babafc",
  "target": "00be1b50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babb04`](#insn-00babb04)

~~~json
{
  "source": "00babb04",
  "target": "00babb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb0c`](#insn-00babb0c)

~~~json
{
  "source": "00babb0c",
  "target": "00be1580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babb18`](#insn-00babb18)

~~~json
{
  "source": "00babb18",
  "target": "00babb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb20`](#insn-00babb20)

~~~json
{
  "source": "00babb20",
  "target": "00babb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb34`](#insn-00babb34)

~~~json
{
  "source": "00babb34",
  "target": "00babb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb3c`](#insn-00babb3c)

~~~json
{
  "source": "00babb3c",
  "target": "00babb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb40`](#insn-00babb40)

~~~json
{
  "source": "00babb40",
  "target": "00babb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb60`](#insn-00babb60)

~~~json
{
  "source": "00babb60",
  "target": "00babb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb68`](#insn-00babb68)

~~~json
{
  "source": "00babb68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb6c`](#insn-00babb6c)

~~~json
{
  "source": "00babb6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb70`](#insn-00babb70)

~~~json
{
  "source": "00babb70",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
