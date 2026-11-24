# 00afa0ec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00af9cc4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af9cc4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-5a872a3cf51bd256868e2e55c7889ea6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afa188`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afa188.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0067.md#compare-e224c3a64cc8b932c1fb63785383bdb1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afa0ec",
  "name": "FUN_00afa0ec",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "88e97c4bd94636d186d2590cb8a6b4af33041485ae369ae8bdd16dca8a10dc4a",
  "source_text_sha256": "88e97c4bd94636d186d2590cb8a6b4af33041485ae369ae8bdd16dca8a10dc4a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afa0ec",
        "00afa1cb"
      ]
    ],
    "bytes_sha256": "c7db2852f86f67f5336809705b28eb7ef33dd4a4961e9c074ecfb563ad56d3c1",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007119f0](../00711/007119f0.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1107 bytes

~~~c

undefined4 FUN_00afa0ec(int param_1,int param_2)

{
  undefined4 uVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514f8();
  uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    uVar1 = 0;
  }
  else {
    lVar2 = FUN_008514f8();
                    /* try { // try from 00afa138 to 00bfa15b has its CatchHandler @ 00afa9d0 */
    uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
                    /* try { // try from 00afa164 to 00bfa16b has its CatchHandler @ 00afaab0 */
    if ((((uVar3 & 1) == 0) ||
        (lVar2 = FUN_008514f8(),
        *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bdc) == 0)) ||
       (lVar2 = FUN_008514f8(),
       *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c60) != 0)) {
      lVar2 = FUN_008514f8();
      uVar1 = *(undefined4 *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c60);
    }
    else {
      uVar1 = 0x46;
                    /* try { // try from 00afa1c8 to 00bfa1cf has its CatchHandler @ 00afa9cc */
    }
  }
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afa0ec"></a> `00afa0ec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afa0f0"></a> `00afa0f0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afa0f4"></a> `00afa0f4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afa0f8"></a> `00afa0f8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afa0fc"></a> `00afa0fc` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afa100"></a> `00afa100` | `fe 5c f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afa104"></a> `00afa104` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afa108"></a> `00afa108` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afa10c"></a> `00afa10c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afa110"></a> `00afa110` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afa114"></a> `00afa114` | `c3 b4 eb 97` | bl 0x005e7420 | `UNCONDITIONAL_CALL`
<a id="insn-00afa118"></a> `00afa118` | `60 00 00 37` | tbnz w0,#0x0,0x00afa124 | `CONDITIONAL_JUMP`
<a id="insn-00afa11c"></a> `00afa11c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afa120"></a> `00afa120` | `26 00 00 14` | b 0x00afa1b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afa124"></a> `00afa124` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00afa128"></a> `00afa128` | `f4 5c f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afa12c"></a> `00afa12c` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00afa130"></a> `00afa130` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00afa134"></a> `00afa134` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afa138"></a> `00afa138` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00afa13c"></a> `00afa13c` | `b9 b4 eb 97` | bl 0x005e7420 | `UNCONDITIONAL_CALL`
<a id="insn-00afa140"></a> `00afa140` | `60 00 00 37` | tbnz w0,#0x0,0x00afa14c | `CONDITIONAL_JUMP`
<a id="insn-00afa144"></a> `00afa144` | `73 7e 40 93` | sxtw x19,w19 | `FALL_THROUGH`
<a id="insn-00afa148"></a> `00afa148` | `14 00 00 14` | b 0x00afa198 | `UNCONDITIONAL_JUMP`
<a id="insn-00afa14c"></a> `00afa14c` | `eb 5c f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afa150"></a> `00afa150` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afa154"></a> `00afa154` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afa158"></a> `00afa158` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afa15c"></a> `00afa15c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afa160"></a> `00afa160` | `89 7b 89 52` | mov w9,#0x4bdc | `FALL_THROUGH`
<a id="insn-00afa164"></a> `00afa164` | `73 7e 40 93` | sxtw x19,w19 | `FALL_THROUGH`
<a id="insn-00afa168"></a> `00afa168` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afa16c"></a> `00afa16c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afa170"></a> `00afa170` | `48 01 00 34` | cbz w8,0x00afa198 | `CONDITIONAL_JUMP`
<a id="insn-00afa174"></a> `00afa174` | `e1 5c f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afa178"></a> `00afa178` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afa17c"></a> `00afa17c` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afa180"></a> `00afa180` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afa184"></a> `00afa184` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afa188"></a> `00afa188` | `09 8c 89 52` | mov w9,#0x4c60 | `FALL_THROUGH`
<a id="insn-00afa18c"></a> `00afa18c` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afa190"></a> `00afa190` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afa194"></a> `00afa194` | `88 01 00 34` | cbz w8,0x00afa1c4 | `CONDITIONAL_JUMP`
<a id="insn-00afa198"></a> `00afa198` | `d8 5c f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afa19c"></a> `00afa19c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afa1a0"></a> `00afa1a0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afa1a4"></a> `00afa1a4` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afa1a8"></a> `00afa1a8` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afa1ac"></a> `00afa1ac` | `09 8c 89 52` | mov w9,#0x4c60 | `FALL_THROUGH`
<a id="insn-00afa1b0"></a> `00afa1b0` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afa1b4"></a> `00afa1b4` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afa1b8"></a> `00afa1b8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afa1bc"></a> `00afa1bc` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afa1c0"></a> `00afa1c0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afa1c4"></a> `00afa1c4` | `c0 08 80 52` | mov w0,#0x46 | `FALL_THROUGH`
<a id="insn-00afa1c8"></a> `00afa1c8` | `fc ff ff 17` | b 0x00afa1b8 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00afa0ec`](#insn-00afa0ec) 範囲 `[['00afa0ec', '00afa11b']]`
  - `CONDITIONAL_JUMP` [`00afa118`](#insn-00afa118) → [`00afa124`](#insn-00afa124)
  - `FALL_THROUGH` [`00afa118`](#insn-00afa118) → [`00afa11c`](#insn-00afa11c)
- ブロック [`00afa11c`](#insn-00afa11c) 範囲 `[['00afa11c', '00afa123']]`
  - `UNCONDITIONAL_JUMP` [`00afa120`](#insn-00afa120) → [`00afa1b8`](#insn-00afa1b8)
- ブロック [`00afa124`](#insn-00afa124) 範囲 `[['00afa124', '00afa137']]`
  - `FALL_THROUGH` [`00afa134`](#insn-00afa134) → [`00afa138`](#insn-00afa138)
- ブロック [`00afa138`](#insn-00afa138) 範囲 `[['00afa138', '00afa143']]`
  - `CONDITIONAL_JUMP` [`00afa140`](#insn-00afa140) → [`00afa14c`](#insn-00afa14c)
  - `FALL_THROUGH` [`00afa140`](#insn-00afa140) → [`00afa144`](#insn-00afa144)
- ブロック [`00afa144`](#insn-00afa144) 範囲 `[['00afa144', '00afa14b']]`
  - `UNCONDITIONAL_JUMP` [`00afa148`](#insn-00afa148) → [`00afa198`](#insn-00afa198)
- ブロック [`00afa14c`](#insn-00afa14c) 範囲 `[['00afa14c', '00afa163']]`
  - `FALL_THROUGH` [`00afa160`](#insn-00afa160) → [`00afa164`](#insn-00afa164)
- ブロック [`00afa164`](#insn-00afa164) 範囲 `[['00afa164', '00afa173']]`
  - `CONDITIONAL_JUMP` [`00afa170`](#insn-00afa170) → [`00afa198`](#insn-00afa198)
  - `FALL_THROUGH` [`00afa170`](#insn-00afa170) → [`00afa174`](#insn-00afa174)
- ブロック [`00afa174`](#insn-00afa174) 範囲 `[['00afa174', '00afa197']]`
  - `CONDITIONAL_JUMP` [`00afa194`](#insn-00afa194) → [`00afa1c4`](#insn-00afa1c4)
  - `FALL_THROUGH` [`00afa194`](#insn-00afa194) → [`00afa198`](#insn-00afa198)
- ブロック [`00afa198`](#insn-00afa198) 範囲 `[['00afa198', '00afa1b7']]`
  - `FALL_THROUGH` [`00afa1b4`](#insn-00afa1b4) → [`00afa1b8`](#insn-00afa1b8)
- ブロック [`00afa1b8`](#insn-00afa1b8) 範囲 `[['00afa1b8', '00afa1c3']]`
- ブロック [`00afa1c4`](#insn-00afa1c4) 範囲 `[['00afa1c4', '00afa1c7']]`
  - `FALL_THROUGH` [`00afa1c4`](#insn-00afa1c4) → [`00afa1c8`](#insn-00afa1c8)
- ブロック [`00afa1c8`](#insn-00afa1c8) 範囲 `[['00afa1c8', '00afa1cb']]`
  - `UNCONDITIONAL_JUMP` [`00afa1c8`](#insn-00afa1c8) → [`00afa1b8`](#insn-00afa1b8)

## 命令位置別の参照

- [`00afa0ec`](#insn-00afa0ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa0f0`](#insn-00afa0f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa100`](#insn-00afa100) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afa114`](#insn-00afa114) → [`005e7420`](../005e7/005e7420.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7420` · 推定シンボル `None` · 推定型 `None`
- [`00afa118`](#insn-00afa118) → [`00afa124`](#insn-00afa124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa120`](#insn-00afa120) → [`00afa1b8`](#insn-00afa1b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa128`](#insn-00afa128) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afa13c`](#insn-00afa13c) → [`005e7420`](../005e7/005e7420.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7420` · 推定シンボル `None` · 推定型 `None`
- [`00afa140`](#insn-00afa140) → [`00afa14c`](#insn-00afa14c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa148`](#insn-00afa148) → [`00afa198`](#insn-00afa198) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa14c`](#insn-00afa14c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afa170`](#insn-00afa170) → [`00afa198`](#insn-00afa198) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa174`](#insn-00afa174) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afa194`](#insn-00afa194) → [`00afa1c4`](#insn-00afa1c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa198`](#insn-00afa198) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afa1b8`](#insn-00afa1b8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa1bc`](#insn-00afa1bc) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa1c8`](#insn-00afa1c8) → [`00afa1b8`](#insn-00afa1b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afa0ec`](#insn-00afa0ec)

~~~json
{
  "source": "00afa0ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa0f0`](#insn-00afa0f0)

~~~json
{
  "source": "00afa0f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa100`](#insn-00afa100)

~~~json
{
  "source": "00afa100",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa114`](#insn-00afa114)

~~~json
{
  "source": "00afa114",
  "target": "005e7420",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa118`](#insn-00afa118)

~~~json
{
  "source": "00afa118",
  "target": "00afa124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa120`](#insn-00afa120)

~~~json
{
  "source": "00afa120",
  "target": "00afa1b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa128`](#insn-00afa128)

~~~json
{
  "source": "00afa128",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa13c`](#insn-00afa13c)

~~~json
{
  "source": "00afa13c",
  "target": "005e7420",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa140`](#insn-00afa140)

~~~json
{
  "source": "00afa140",
  "target": "00afa14c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa148`](#insn-00afa148)

~~~json
{
  "source": "00afa148",
  "target": "00afa198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa14c`](#insn-00afa14c)

~~~json
{
  "source": "00afa14c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa170`](#insn-00afa170)

~~~json
{
  "source": "00afa170",
  "target": "00afa198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa174`](#insn-00afa174)

~~~json
{
  "source": "00afa174",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa194`](#insn-00afa194)

~~~json
{
  "source": "00afa194",
  "target": "00afa1c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa198`](#insn-00afa198)

~~~json
{
  "source": "00afa198",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afa1b8`](#insn-00afa1b8)

~~~json
{
  "source": "00afa1b8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa1bc`](#insn-00afa1bc)

~~~json
{
  "source": "00afa1bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa1c8`](#insn-00afa1c8)

~~~json
{
  "source": "00afa1c8",
  "target": "00afa1b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
