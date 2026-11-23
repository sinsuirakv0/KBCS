# 00aa1afc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aa1afc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1afc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0025.md#compare-64099ba5b06b4cbcd9575e7c2e27ca05)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa1afc",
  "name": "FUN_00aa1afc",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e52a40355037386c8c69568354c35fb69392c4bb6948d5469e1a30c3a57aaa98",
  "source_text_sha256": "e52a40355037386c8c69568354c35fb69392c4bb6948d5469e1a30c3a57aaa98",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa1afc",
        "00aa1b8f"
      ]
    ],
    "bytes_sha256": "77737938a2be1006822591b73578d9ad9eb48d8916c2f90eb88e03db04610d9d",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0065f258](../0065f/0065f258.md)
- [006a0ab4](../006a0/006a0ab4.md)
- [009f1e64](../009f1/009f1e64.md)
- [00aa0f20](../00aa0/00aa0f20.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)
- [00aa2c2c](../00aa2/00aa2c2c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5416 bytes

~~~c

undefined8 FUN_00aa1afc(int param_1,int param_2,int param_3)

{
  long lVar1;
  ulong uVar2;
  undefined8 uVar3;
  
                    /* catch() { ... } // from try @ 00aa0f74 with catch @ 00aa1b08 */
                    /* catch() { ... } // from try @ 00a9ffc8 with catch @ 00aa1b0c */
                    /* catch() { ... } // from try @ 00a9feb4 with catch @ 00aa1b10 */
  lVar1 = FUN_0081f580();
                    /* catch() { ... } // from try @ 00aa052c with catch @ 00aa1b28 */
                    /* catch() { ... } // from try @ 00aa0020 with catch @ 00aa1b2c */
  uVar2 = FUN_005c2710(lVar1 + (long)param_1 * 0x1f0 + 0x2678);
                    /* catch() { ... } // from try @ 00aa0674 with catch @ 00aa1b30 */
  if ((uVar2 & 1) == 0) {
                    /* catch() { ... } // from try @ 00aa1774 with catch @ 00aa1b34 */
    uVar3 = 0;
                    /* catch() { ... } // from try @ 00aa0984 with catch @ 00aa1b38 */
  }
  else {
                    /* catch() { ... } // from try @ 00aa0108 with catch @ 00aa1b3c */
    lVar1 = FUN_0081f580();
                    /* catch() { ... } // from try @ 00aa0708 with catch @ 00aa1b40 */
                    /* catch() { ... } // from try @ 00aa16e4 with catch @ 00aa1b44 */
                    /* catch() { ... } // from try @ 00a9ffa8 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0018 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0224 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa032c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0408 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0524 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa05b0 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0654 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa06c8 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa08e4 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0a8c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0b4c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0b9c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0c3c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0c8c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0ce4 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0e00 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0e54 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0ec4 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa0f9c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1004 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa105c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa10b4 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa110c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1164 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa11bc with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1214 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1294 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa12ec with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1344 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa13ac with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1404 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa145c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa14b4 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa150c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1564 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa15bc with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1614 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa166c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa170c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa179c with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa17f8 with catch @ 00aa1b48
                       catch() { ... } // from try @ 00aa1860 with catch @ 00aa1b48 */
                    /* catch() { ... } // from try @ 00aa07f0 with catch @ 00aa1b4c */
                    /* catch() { ... } // from try @ 00aa0114 with catch @ 00aa1b50 */
                    /* catch() { ... } // from try @ 00aa093c with catch @ 00aa1b54 */
                    /* catch() { ... } // from try @ 00aa07fc with catch @ 00aa1b58 */
    if (*(int *)(lVar1 + (long)param_2 * 0x770 + (long)param_3 * 0x1dc + 0x9fddc) == 0) {
      uVar3 = FUN_00aa2c2c(lVar1,param_2,param_3,6);
      return uVar3;
    }
    uVar3 = 1;
  }
  return uVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa1afc"></a> `00aa1afc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aa1b00"></a> `00aa1b00` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1b04"></a> `00aa1b04` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa1b08"></a> `00aa1b08` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa1b0c"></a> `00aa1b0c` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00aa1b10"></a> `00aa1b10` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aa1b14"></a> `00aa1b14` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aa1b18"></a> `00aa1b18` | `9a f6 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1b1c"></a> `00aa1b1c` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00aa1b20"></a> `00aa1b20` | `09 cf 84 52` | mov w9,#0x2678 | `FALL_THROUGH`
<a id="insn-00aa1b24"></a> `00aa1b24` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa1b28"></a> `00aa1b28` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00aa1b2c"></a> `00aa1b2c` | `f9 82 ec 97` | bl 0x005c2710 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1b30"></a> `00aa1b30` | `60 00 00 37` | tbnz w0,#0x0,0x00aa1b3c | `CONDITIONAL_JUMP`
<a id="insn-00aa1b34"></a> `00aa1b34` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aa1b38"></a> `00aa1b38` | `0b 00 00 14` | b 0x00aa1b64 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa1b3c"></a> `00aa1b3c` | `91 f6 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1b40"></a> `00aa1b40` | `08 ee 80 52` | mov w8,#0x770 | `FALL_THROUGH`
<a id="insn-00aa1b44"></a> `00aa1b44` | `89 3b 80 52` | mov w9,#0x1dc | `FALL_THROUGH`
<a id="insn-00aa1b48"></a> `00aa1b48` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00aa1b4c"></a> `00aa1b4c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00aa1b50"></a> `00aa1b50` | `89 bb 9f 52` | mov w9,#0xfddc | `FALL_THROUGH`
<a id="insn-00aa1b54"></a> `00aa1b54` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa1b58"></a> `00aa1b58` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aa1b5c"></a> `00aa1b5c` | `c8 00 00 34` | cbz w8,0x00aa1b74 | `CONDITIONAL_JUMP`
<a id="insn-00aa1b60"></a> `00aa1b60` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aa1b64"></a> `00aa1b64` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa1b68"></a> `00aa1b68` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1b6c"></a> `00aa1b6c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa1b70"></a> `00aa1b70` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa1b74"></a> `00aa1b74` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aa1b78"></a> `00aa1b78` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00aa1b7c"></a> `00aa1b7c` | `c3 00 80 52` | mov w3,#0x6 | `FALL_THROUGH`
<a id="insn-00aa1b80"></a> `00aa1b80` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa1b84"></a> `00aa1b84` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1b88"></a> `00aa1b88` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aa1b8c"></a> `00aa1b8c` | `28 04 00 14` | b 0x00aa2c2c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa1afc`](#insn-00aa1afc) 範囲 `[['00aa1afc', '00aa1b07']]`
  - `FALL_THROUGH` [`00aa1b04`](#insn-00aa1b04) → [`00aa1b08`](#insn-00aa1b08)
- ブロック [`00aa1b08`](#insn-00aa1b08) 範囲 `[['00aa1b08', '00aa1b0b']]`
  - `FALL_THROUGH` [`00aa1b08`](#insn-00aa1b08) → [`00aa1b0c`](#insn-00aa1b0c)
- ブロック [`00aa1b0c`](#insn-00aa1b0c) 範囲 `[['00aa1b0c', '00aa1b0f']]`
  - `FALL_THROUGH` [`00aa1b0c`](#insn-00aa1b0c) → [`00aa1b10`](#insn-00aa1b10)
- ブロック [`00aa1b10`](#insn-00aa1b10) 範囲 `[['00aa1b10', '00aa1b27']]`
  - `FALL_THROUGH` [`00aa1b24`](#insn-00aa1b24) → [`00aa1b28`](#insn-00aa1b28)
- ブロック [`00aa1b28`](#insn-00aa1b28) 範囲 `[['00aa1b28', '00aa1b2b']]`
  - `FALL_THROUGH` [`00aa1b28`](#insn-00aa1b28) → [`00aa1b2c`](#insn-00aa1b2c)
- ブロック [`00aa1b2c`](#insn-00aa1b2c) 範囲 `[['00aa1b2c', '00aa1b2f']]`
  - `FALL_THROUGH` [`00aa1b2c`](#insn-00aa1b2c) → [`00aa1b30`](#insn-00aa1b30)
- ブロック [`00aa1b30`](#insn-00aa1b30) 範囲 `[['00aa1b30', '00aa1b33']]`
  - `CONDITIONAL_JUMP` [`00aa1b30`](#insn-00aa1b30) → [`00aa1b3c`](#insn-00aa1b3c)
  - `FALL_THROUGH` [`00aa1b30`](#insn-00aa1b30) → [`00aa1b34`](#insn-00aa1b34)
- ブロック [`00aa1b34`](#insn-00aa1b34) 範囲 `[['00aa1b34', '00aa1b37']]`
  - `FALL_THROUGH` [`00aa1b34`](#insn-00aa1b34) → [`00aa1b38`](#insn-00aa1b38)
- ブロック [`00aa1b38`](#insn-00aa1b38) 範囲 `[['00aa1b38', '00aa1b3b']]`
  - `UNCONDITIONAL_JUMP` [`00aa1b38`](#insn-00aa1b38) → [`00aa1b64`](#insn-00aa1b64)
- ブロック [`00aa1b3c`](#insn-00aa1b3c) 範囲 `[['00aa1b3c', '00aa1b3f']]`
  - `FALL_THROUGH` [`00aa1b3c`](#insn-00aa1b3c) → [`00aa1b40`](#insn-00aa1b40)
- ブロック [`00aa1b40`](#insn-00aa1b40) 範囲 `[['00aa1b40', '00aa1b43']]`
  - `FALL_THROUGH` [`00aa1b40`](#insn-00aa1b40) → [`00aa1b44`](#insn-00aa1b44)
- ブロック [`00aa1b44`](#insn-00aa1b44) 範囲 `[['00aa1b44', '00aa1b47']]`
  - `FALL_THROUGH` [`00aa1b44`](#insn-00aa1b44) → [`00aa1b48`](#insn-00aa1b48)
- ブロック [`00aa1b48`](#insn-00aa1b48) 範囲 `[['00aa1b48', '00aa1b4b']]`
  - `FALL_THROUGH` [`00aa1b48`](#insn-00aa1b48) → [`00aa1b4c`](#insn-00aa1b4c)
- ブロック [`00aa1b4c`](#insn-00aa1b4c) 範囲 `[['00aa1b4c', '00aa1b4f']]`
  - `FALL_THROUGH` [`00aa1b4c`](#insn-00aa1b4c) → [`00aa1b50`](#insn-00aa1b50)
- ブロック [`00aa1b50`](#insn-00aa1b50) 範囲 `[['00aa1b50', '00aa1b53']]`
  - `FALL_THROUGH` [`00aa1b50`](#insn-00aa1b50) → [`00aa1b54`](#insn-00aa1b54)
- ブロック [`00aa1b54`](#insn-00aa1b54) 範囲 `[['00aa1b54', '00aa1b57']]`
  - `FALL_THROUGH` [`00aa1b54`](#insn-00aa1b54) → [`00aa1b58`](#insn-00aa1b58)
- ブロック [`00aa1b58`](#insn-00aa1b58) 範囲 `[['00aa1b58', '00aa1b5f']]`
  - `CONDITIONAL_JUMP` [`00aa1b5c`](#insn-00aa1b5c) → [`00aa1b74`](#insn-00aa1b74)
  - `FALL_THROUGH` [`00aa1b5c`](#insn-00aa1b5c) → [`00aa1b60`](#insn-00aa1b60)
- ブロック [`00aa1b60`](#insn-00aa1b60) 範囲 `[['00aa1b60', '00aa1b63']]`
  - `FALL_THROUGH` [`00aa1b60`](#insn-00aa1b60) → [`00aa1b64`](#insn-00aa1b64)
- ブロック [`00aa1b64`](#insn-00aa1b64) 範囲 `[['00aa1b64', '00aa1b73']]`
- ブロック [`00aa1b74`](#insn-00aa1b74) 範囲 `[['00aa1b74', '00aa1b8f']]`

## 命令位置別の参照

- [`00aa1afc`](#insn-00aa1afc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b00`](#insn-00aa1b00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b04`](#insn-00aa1b04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b18`](#insn-00aa1b18) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b2c`](#insn-00aa1b2c) → [`005c2710`](../005c2/005c2710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c2710` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b30`](#insn-00aa1b30) → [`00aa1b3c`](#insn-00aa1b3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b38`](#insn-00aa1b38) → [`00aa1b64`](#insn-00aa1b64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b3c`](#insn-00aa1b3c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b5c`](#insn-00aa1b5c) → [`00aa1b74`](#insn-00aa1b74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b64`](#insn-00aa1b64) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b68`](#insn-00aa1b68) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b6c`](#insn-00aa1b6c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b80`](#insn-00aa1b80) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b84`](#insn-00aa1b84) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b88`](#insn-00aa1b88) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1b8c`](#insn-00aa1b8c) → [`00aa2c2c`](../00aa2/00aa2c2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aa2c2c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa1afc`](#insn-00aa1afc)

~~~json
{
  "source": "00aa1afc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b00`](#insn-00aa1b00)

~~~json
{
  "source": "00aa1b00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b04`](#insn-00aa1b04)

~~~json
{
  "source": "00aa1b04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b18`](#insn-00aa1b18)

~~~json
{
  "source": "00aa1b18",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1b2c`](#insn-00aa1b2c)

~~~json
{
  "source": "00aa1b2c",
  "target": "005c2710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1b30`](#insn-00aa1b30)

~~~json
{
  "source": "00aa1b30",
  "target": "00aa1b3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b38`](#insn-00aa1b38)

~~~json
{
  "source": "00aa1b38",
  "target": "00aa1b64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b3c`](#insn-00aa1b3c)

~~~json
{
  "source": "00aa1b3c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1b5c`](#insn-00aa1b5c)

~~~json
{
  "source": "00aa1b5c",
  "target": "00aa1b74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b64`](#insn-00aa1b64)

~~~json
{
  "source": "00aa1b64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b68`](#insn-00aa1b68)

~~~json
{
  "source": "00aa1b68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b6c`](#insn-00aa1b6c)

~~~json
{
  "source": "00aa1b6c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b80`](#insn-00aa1b80)

~~~json
{
  "source": "00aa1b80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b84`](#insn-00aa1b84)

~~~json
{
  "source": "00aa1b84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b88`](#insn-00aa1b88)

~~~json
{
  "source": "00aa1b88",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1b8c`](#insn-00aa1b8c)

~~~json
{
  "source": "00aa1b8c",
  "target": "00aa2c2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
