# 00c2abec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bae1a4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae1a4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-efa0019c9daa8a00308b52ef83eacd61)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c2b014`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2b/00c2b014.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0009.md#compare-d6d1383d924711641d966df79812a3f4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2abec",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb1EE9do_lengthER9mbstate_tPKcS5_m",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b855bd549ed9029714d4888cfb0ac7662c2c19fb5390bf28221661e63553db50",
  "source_text_sha256": "b855bd549ed9029714d4888cfb0ac7662c2c19fb5390bf28221661e63553db50",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c2abec",
        "00c2ac7f"
      ]
    ],
    "bytes_sha256": "63b61024d973bf051d4ab6d854a9dacb01836ecae8e811f479e89252931dcde3",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1639 bytes

~~~c

int _ZNKSt6__ndk115__codecvt_utf16IDsLb1EE9do_lengthER9mbstate_tPKcS5_m
              (long param_1,undefined8 param_2,char *param_3,long param_4,ulong param_5)

{
  bool bVar1;
  bool bVar2;
  int iVar3;
  ulong uVar4;
  
  iVar3 = (int)param_3;
                    /* try { // try from 00c2ac08 to 00d2ac0f has its CatchHandler @ 00c2ac1c */
                    /* catch() { ... } // from try @ 00c2abac with catch @ 00c2ac10
                       try { // try from 00c2ac10 to 00d2ac47 has its CatchHandler @ 00c2ab20 */
  if (((1 < param_4 - (long)param_3) && ((*(uint *)(param_1 + 0x18) >> 2 & 1) != 0)) &&
     (*param_3 == -1)) {
                    /* catch() { ... } // from try @ 00c2ab94 with catch @ 00c2ac1c
                       catch() { ... } // from try @ 00c2ac08 with catch @ 00c2ac1c */
    param_3 = param_3 + (ulong)(param_3[1] == -2) * 2;
  }
  if ((param_5 != 0) && (param_3 < (char *)(param_4 + -1))) {
    uVar4 = 1;
    do {
                    /* try { // try from 00c2ac48 to 00d2ad47 has its CatchHandler @ 00c2ac48
                       catch() { ... } // from try @ 00c2ac48 with catch @ 00c2ac48
                       catch() { ... } // from try @ 00c2ad90 with catch @ 00c2ac48
                       catch() { ... } // from try @ 00c2ae88 with catch @ 00c2ac48 */
      if ((param_3[1] & 0xf8U) == 0xd8) break;
      bVar1 = (ulong)CONCAT11(param_3[1],*param_3) <= *(ulong *)(param_1 + 0x10);
      param_3 = param_3 + (ulong)bVar1 * 2;
      bVar2 = uVar4 < param_5;
      uVar4 = uVar4 + 1;
    } while ((bVar1 && param_3 < (char *)(param_4 + -1)) && bVar2);
  }
  return (int)param_3 - iVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c2abec"></a> `00c2abec` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00c2abf0"></a> `00c2abf0` | `68 00 02 cb` | sub x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00c2abf4"></a> `00c2abf4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c2abf8"></a> `00c2abf8` | `e8 03 02 aa` | mov x8,x2 | `FALL_THROUGH`
<a id="insn-00c2abfc"></a> `00c2abfc` | `8b 01 00 54` | b.lt 0x00c2ac2c | `CONDITIONAL_JUMP`
<a id="insn-00c2ac00"></a> `00c2ac00` | `09 18 40 b9` | ldr w9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00c2ac04"></a> `00c2ac04` | `e8 03 02 aa` | mov x8,x2 | `FALL_THROUGH`
<a id="insn-00c2ac08"></a> `00c2ac08` | `29 01 10 36` | tbz w9,#0x2,0x00c2ac2c | `CONDITIONAL_JUMP`
<a id="insn-00c2ac0c"></a> `00c2ac0c` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00c2ac10"></a> `00c2ac10` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00c2ac14"></a> `00c2ac14` | `e8 03 02 aa` | mov x8,x2 | `FALL_THROUGH`
<a id="insn-00c2ac18"></a> `00c2ac18` | `a1 00 00 54` | b.ne 0x00c2ac2c | `CONDITIONAL_JUMP`
<a id="insn-00c2ac1c"></a> `00c2ac1c` | `48 04 40 39` | ldrb w8,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00c2ac20"></a> `00c2ac20` | `1f f9 03 71` | cmp w8,#0xfe | `FALL_THROUGH`
<a id="insn-00c2ac24"></a> `00c2ac24` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00c2ac28"></a> `00c2ac28` | `48 44 28 8b` | add x8,x2,w8, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00c2ac2c"></a> `00c2ac2c` | `64 02 00 b4` | cbz x4,0x00c2ac78 | `CONDITIONAL_JUMP`
<a id="insn-00c2ac30"></a> `00c2ac30` | `69 04 00 d1` | sub x9,x3,#0x1 | `FALL_THROUGH`
<a id="insn-00c2ac34"></a> `00c2ac34` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c2ac38"></a> `00c2ac38` | `02 02 00 54` | b.cs 0x00c2ac78 | `CONDITIONAL_JUMP`
<a id="insn-00c2ac3c"></a> `00c2ac3c` | `0a 08 40 f9` | ldr x10,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c2ac40"></a> `00c2ac40` | `2b 00 80 52` | mov w11,#0x1 | `FALL_THROUGH`
<a id="insn-00c2ac44"></a> `00c2ac44` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00c2ac48"></a> `00c2ac48` | `8d 11 1d 12` | and w13,w12,#0xf8 | `FALL_THROUGH`
<a id="insn-00c2ac4c"></a> `00c2ac4c` | `bf 61 03 71` | cmp w13,#0xd8 | `FALL_THROUGH`
<a id="insn-00c2ac50"></a> `00c2ac50` | `40 01 00 54` | b.eq 0x00c2ac78 | `CONDITIONAL_JUMP`
<a id="insn-00c2ac54"></a> `00c2ac54` | `0d 01 40 39` | ldrb w13,[x8] | `FALL_THROUGH`
<a id="insn-00c2ac58"></a> `00c2ac58` | `ac 21 0c 2a` | orr w12,w13,w12, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00c2ac5c"></a> `00c2ac5c` | `5f 01 0c eb` | cmp x10,x12 | `FALL_THROUGH`
<a id="insn-00c2ac60"></a> `00c2ac60` | `ec 37 9f 1a` | cset w12,cs | `FALL_THROUGH`
<a id="insn-00c2ac64"></a> `00c2ac64` | `08 45 2c 8b` | add x8,x8,w12, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00c2ac68"></a> `00c2ac68` | `02 21 49 fa` | ccmp x8,x9,#0x2,cs | `FALL_THROUGH`
<a id="insn-00c2ac6c"></a> `00c2ac6c` | `62 31 44 fa` | ccmp x11,x4,#0x2,cc | `FALL_THROUGH`
<a id="insn-00c2ac70"></a> `00c2ac70` | `6b 05 00 91` | add x11,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00c2ac74"></a> `00c2ac74` | `83 fe ff 54` | b.cc 0x00c2ac44 | `CONDITIONAL_JUMP`
<a id="insn-00c2ac78"></a> `00c2ac78` | `00 01 02 4b` | sub w0,w8,w2 | `FALL_THROUGH`
<a id="insn-00c2ac7c"></a> `00c2ac7c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c2abec`](#insn-00c2abec) 範囲 `[['00c2abec', '00c2abff']]`
  - `CONDITIONAL_JUMP` [`00c2abfc`](#insn-00c2abfc) → [`00c2ac2c`](#insn-00c2ac2c)
  - `FALL_THROUGH` [`00c2abfc`](#insn-00c2abfc) → [`00c2ac00`](#insn-00c2ac00)
- ブロック [`00c2ac00`](#insn-00c2ac00) 範囲 `[['00c2ac00', '00c2ac07']]`
  - `FALL_THROUGH` [`00c2ac04`](#insn-00c2ac04) → [`00c2ac08`](#insn-00c2ac08)
- ブロック [`00c2ac08`](#insn-00c2ac08) 範囲 `[['00c2ac08', '00c2ac0b']]`
  - `CONDITIONAL_JUMP` [`00c2ac08`](#insn-00c2ac08) → [`00c2ac2c`](#insn-00c2ac2c)
  - `FALL_THROUGH` [`00c2ac08`](#insn-00c2ac08) → [`00c2ac0c`](#insn-00c2ac0c)
- ブロック [`00c2ac0c`](#insn-00c2ac0c) 範囲 `[['00c2ac0c', '00c2ac0f']]`
  - `FALL_THROUGH` [`00c2ac0c`](#insn-00c2ac0c) → [`00c2ac10`](#insn-00c2ac10)
- ブロック [`00c2ac10`](#insn-00c2ac10) 範囲 `[['00c2ac10', '00c2ac1b']]`
  - `CONDITIONAL_JUMP` [`00c2ac18`](#insn-00c2ac18) → [`00c2ac2c`](#insn-00c2ac2c)
  - `FALL_THROUGH` [`00c2ac18`](#insn-00c2ac18) → [`00c2ac1c`](#insn-00c2ac1c)
- ブロック [`00c2ac1c`](#insn-00c2ac1c) 範囲 `[['00c2ac1c', '00c2ac2b']]`
  - `FALL_THROUGH` [`00c2ac28`](#insn-00c2ac28) → [`00c2ac2c`](#insn-00c2ac2c)
- ブロック [`00c2ac2c`](#insn-00c2ac2c) 範囲 `[['00c2ac2c', '00c2ac2f']]`
  - `CONDITIONAL_JUMP` [`00c2ac2c`](#insn-00c2ac2c) → [`00c2ac78`](#insn-00c2ac78)
  - `FALL_THROUGH` [`00c2ac2c`](#insn-00c2ac2c) → [`00c2ac30`](#insn-00c2ac30)
- ブロック [`00c2ac30`](#insn-00c2ac30) 範囲 `[['00c2ac30', '00c2ac3b']]`
  - `CONDITIONAL_JUMP` [`00c2ac38`](#insn-00c2ac38) → [`00c2ac78`](#insn-00c2ac78)
  - `FALL_THROUGH` [`00c2ac38`](#insn-00c2ac38) → [`00c2ac3c`](#insn-00c2ac3c)
- ブロック [`00c2ac3c`](#insn-00c2ac3c) 範囲 `[['00c2ac3c', '00c2ac43']]`
  - `FALL_THROUGH` [`00c2ac40`](#insn-00c2ac40) → [`00c2ac44`](#insn-00c2ac44)
- ブロック [`00c2ac44`](#insn-00c2ac44) 範囲 `[['00c2ac44', '00c2ac47']]`
  - `FALL_THROUGH` [`00c2ac44`](#insn-00c2ac44) → [`00c2ac48`](#insn-00c2ac48)
- ブロック [`00c2ac48`](#insn-00c2ac48) 範囲 `[['00c2ac48', '00c2ac53']]`
  - `CONDITIONAL_JUMP` [`00c2ac50`](#insn-00c2ac50) → [`00c2ac78`](#insn-00c2ac78)
  - `FALL_THROUGH` [`00c2ac50`](#insn-00c2ac50) → [`00c2ac54`](#insn-00c2ac54)
- ブロック [`00c2ac54`](#insn-00c2ac54) 範囲 `[['00c2ac54', '00c2ac77']]`
  - `CONDITIONAL_JUMP` [`00c2ac74`](#insn-00c2ac74) → [`00c2ac44`](#insn-00c2ac44)
  - `FALL_THROUGH` [`00c2ac74`](#insn-00c2ac74) → [`00c2ac78`](#insn-00c2ac78)
- ブロック [`00c2ac78`](#insn-00c2ac78) 範囲 `[['00c2ac78', '00c2ac7f']]`

## 命令位置別の参照

- [`00c2abfc`](#insn-00c2abfc) → [`00c2ac2c`](#insn-00c2ac2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ac08`](#insn-00c2ac08) → [`00c2ac2c`](#insn-00c2ac2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ac18`](#insn-00c2ac18) → [`00c2ac2c`](#insn-00c2ac2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ac2c`](#insn-00c2ac2c) → [`00c2ac78`](#insn-00c2ac78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ac38`](#insn-00c2ac38) → [`00c2ac78`](#insn-00c2ac78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ac50`](#insn-00c2ac50) → [`00c2ac78`](#insn-00c2ac78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2ac74`](#insn-00c2ac74) → [`00c2ac44`](#insn-00c2ac44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c2abfc`](#insn-00c2abfc)

~~~json
{
  "source": "00c2abfc",
  "target": "00c2ac2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ac08`](#insn-00c2ac08)

~~~json
{
  "source": "00c2ac08",
  "target": "00c2ac2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ac18`](#insn-00c2ac18)

~~~json
{
  "source": "00c2ac18",
  "target": "00c2ac2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ac2c`](#insn-00c2ac2c)

~~~json
{
  "source": "00c2ac2c",
  "target": "00c2ac78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ac38`](#insn-00c2ac38)

~~~json
{
  "source": "00c2ac38",
  "target": "00c2ac78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ac50`](#insn-00c2ac50)

~~~json
{
  "source": "00c2ac50",
  "target": "00c2ac78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2ac74`](#insn-00c2ac74)

~~~json
{
  "source": "00c2ac74",
  "target": "00c2ac44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
