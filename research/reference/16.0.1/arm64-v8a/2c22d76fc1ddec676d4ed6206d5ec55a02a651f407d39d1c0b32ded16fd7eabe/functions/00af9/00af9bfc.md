# 00af9bfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00af97d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af97d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-a669cabfbf1a89a0b3200d560330bca1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af9c98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af9/00af9c98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0067.md#compare-50a038bedf9405a00c935eb12d1f199c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af9bfc",
  "name": "FUN_00af9bfc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b3928f8ce84dd4dba6d4c72cd209fc8702a868d688e63c5f16c05b24f38c4b3e",
  "source_text_sha256": "b3928f8ce84dd4dba6d4c72cd209fc8702a868d688e63c5f16c05b24f38c4b3e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af9bfc",
        "00af9c6b"
      ]
    ],
    "bytes_sha256": "415c58a0fab8441f4f248c6853fbf5c2dfeff900814bdf4a36da9150f2db691c",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0070ea5c](../0070e/0070ea5c.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1095 bytes

~~~c

bool FUN_00af9bfc(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514f8();
                    /* try { // try from 00af9c14 to 00bf9c1b has its CatchHandler @ 00af9c48 */
                    /* catch() { ... } // from try @ 00af9b58 with catch @ 00af9c1c
                       try { // try from 00af9c1c to 00bf9d0f has its CatchHandler @ 00af981c */
  uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
                    /* catch() { ... } // from try @ 00af9944 with catch @ 00af9c34 */
    lVar2 = FUN_008514f8();
                    /* catch() { ... } // from try @ 00af98b4 with catch @ 00af9c48
                       catch() { ... } // from try @ 00af9c14 with catch @ 00af9c48 */
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a78) != 0;
  }
                    /* catch() { ... } // from try @ 00af9868 with catch @ 00af9c60 */
                    /* catch() { ... } // from try @ 00af9854 with catch @ 00af9c68 */
  return bVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af9bfc"></a> `00af9bfc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af9c00"></a> `00af9c00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af9c04"></a> `00af9c04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af9c08"></a> `00af9c08` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00af9c0c"></a> `00af9c0c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00af9c10"></a> `00af9c10` | `3a 5e f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00af9c14"></a> `00af9c14` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00af9c18"></a> `00af9c18` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00af9c1c"></a> `00af9c1c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00af9c20"></a> `00af9c20` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00af9c24"></a> `00af9c24` | `ff b5 eb 97` | bl 0x005e7420 | `UNCONDITIONAL_CALL`
<a id="insn-00af9c28"></a> `00af9c28` | `60 00 00 37` | tbnz w0,#0x0,0x00af9c34 | `CONDITIONAL_JUMP`
<a id="insn-00af9c2c"></a> `00af9c2c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00af9c30"></a> `00af9c30` | `0c 00 00 14` | b 0x00af9c60 | `UNCONDITIONAL_JUMP`
<a id="insn-00af9c34"></a> `00af9c34` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00af9c38"></a> `00af9c38` | `30 5e f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00af9c3c"></a> `00af9c3c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af9c40"></a> `00af9c40` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af9c44"></a> `00af9c44` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00af9c48"></a> `00af9c48` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00af9c4c"></a> `00af9c4c` | `09 4f 89 52` | mov w9,#0x4a78 | `FALL_THROUGH`
<a id="insn-00af9c50"></a> `00af9c50` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af9c54"></a> `00af9c54` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af9c58"></a> `00af9c58` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00af9c5c"></a> `00af9c5c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00af9c60"></a> `00af9c60` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af9c64"></a> `00af9c64` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af9c68"></a> `00af9c68` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af9bfc`](#insn-00af9bfc) 範囲 `[['00af9bfc', '00af9c13']]`
  - `FALL_THROUGH` [`00af9c10`](#insn-00af9c10) → [`00af9c14`](#insn-00af9c14)
- ブロック [`00af9c14`](#insn-00af9c14) 範囲 `[['00af9c14', '00af9c1b']]`
  - `FALL_THROUGH` [`00af9c18`](#insn-00af9c18) → [`00af9c1c`](#insn-00af9c1c)
- ブロック [`00af9c1c`](#insn-00af9c1c) 範囲 `[['00af9c1c', '00af9c2b']]`
  - `CONDITIONAL_JUMP` [`00af9c28`](#insn-00af9c28) → [`00af9c34`](#insn-00af9c34)
  - `FALL_THROUGH` [`00af9c28`](#insn-00af9c28) → [`00af9c2c`](#insn-00af9c2c)
- ブロック [`00af9c2c`](#insn-00af9c2c) 範囲 `[['00af9c2c', '00af9c33']]`
  - `UNCONDITIONAL_JUMP` [`00af9c30`](#insn-00af9c30) → [`00af9c60`](#insn-00af9c60)
- ブロック [`00af9c34`](#insn-00af9c34) 範囲 `[['00af9c34', '00af9c47']]`
  - `FALL_THROUGH` [`00af9c44`](#insn-00af9c44) → [`00af9c48`](#insn-00af9c48)
- ブロック [`00af9c48`](#insn-00af9c48) 範囲 `[['00af9c48', '00af9c5f']]`
  - `FALL_THROUGH` [`00af9c5c`](#insn-00af9c5c) → [`00af9c60`](#insn-00af9c60)
- ブロック [`00af9c60`](#insn-00af9c60) 範囲 `[['00af9c60', '00af9c67']]`
  - `FALL_THROUGH` [`00af9c64`](#insn-00af9c64) → [`00af9c68`](#insn-00af9c68)
- ブロック [`00af9c68`](#insn-00af9c68) 範囲 `[['00af9c68', '00af9c6b']]`

## 命令位置別の参照

- [`00af9bfc`](#insn-00af9bfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9c00`](#insn-00af9c00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9c10`](#insn-00af9c10) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00af9c24`](#insn-00af9c24) → [`005e7420`](../005e7/005e7420.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7420` · 推定シンボル `None` · 推定型 `None`
- [`00af9c28`](#insn-00af9c28) → [`00af9c34`](#insn-00af9c34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9c30`](#insn-00af9c30) → [`00af9c60`](#insn-00af9c60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9c38`](#insn-00af9c38) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00af9c60`](#insn-00af9c60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af9c64`](#insn-00af9c64) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af9bfc`](#insn-00af9bfc)

~~~json
{
  "source": "00af9bfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9c00`](#insn-00af9c00)

~~~json
{
  "source": "00af9c00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9c10`](#insn-00af9c10)

~~~json
{
  "source": "00af9c10",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af9c24`](#insn-00af9c24)

~~~json
{
  "source": "00af9c24",
  "target": "005e7420",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af9c28`](#insn-00af9c28)

~~~json
{
  "source": "00af9c28",
  "target": "00af9c34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9c30`](#insn-00af9c30)

~~~json
{
  "source": "00af9c30",
  "target": "00af9c60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9c38`](#insn-00af9c38)

~~~json
{
  "source": "00af9c38",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af9c60`](#insn-00af9c60)

~~~json
{
  "source": "00af9c60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af9c64`](#insn-00af9c64)

~~~json
{
  "source": "00af9c64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
