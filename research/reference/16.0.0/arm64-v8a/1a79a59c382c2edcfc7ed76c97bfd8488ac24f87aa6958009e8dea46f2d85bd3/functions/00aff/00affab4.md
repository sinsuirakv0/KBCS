# 00affab4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0170.md#review-f0ee45c73d5979ab2be2afaded59d01a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00affedc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00affedc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-4b2c04c0ab5d08a4af66f44f5f678b59)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affab4",
  "name": "FUN_00affab4",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "93ba37caa84ae6c2719cc5d2ce146280b5caf26993abb9ad5657aaabd9c44448",
  "source_text_sha256": "93ba37caa84ae6c2719cc5d2ce146280b5caf26993abb9ad5657aaabd9c44448",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affab4",
        "00affb3b"
      ]
    ],
    "bytes_sha256": "c74833047e631024f70d980011fa239dd2cbf406044baf8a7513cb97050f7fa4",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [005e73e0](../005e7/005e73e0.md)
- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1085 bytes

~~~c

undefined4 FUN_00affab4(int param_1,int param_2,int param_3)

{
  undefined4 *puVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00aff438 with catch @ 00affae4 */
  uVar3 = FUN_005e73e0(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  lVar2 = FUN_008514b8();
                    /* catch() { ... } // from try @ 00aff40c with catch @ 00affaf4 */
                    /* catch() { ... } // from try @ 00aff89c with catch @ 00affb08 */
                    /* catch() { ... } // from try @ 00aff670 with catch @ 00affb10
                       catch() { ... } // from try @ 00aff7c4 with catch @ 00affb10 */
                    /* catch() { ... } // from try @ 00aff630 with catch @ 00affb14 */
                    /* catch() { ... } // from try @ 00aff8e4 with catch @ 00affb18 */
  puVar1 = (undefined4 *)((long)__DT_JMPREL + lVar2 + ((long)param_2 + 2) * 0x1c4 + 0x180c);
  if ((uVar3 & 1) != 0) {
    puVar1 = (undefined4 *)(lVar2 + ((long)param_2 + 2) * 0x770 + (long)param_3 * 0x1dc + 0x9f6e4);
  }
  return *puVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affab4"></a> `00affab4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00affab8"></a> `00affab8` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affabc"></a> `00affabc` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affac0"></a> `00affac0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00affac4"></a> `00affac4` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00affac8"></a> `00affac8` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00affacc"></a> `00affacc` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00affad0"></a> `00affad0` | `7a 46 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affad4"></a> `00affad4` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00affad8"></a> `00affad8` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00affadc"></a> `00affadc` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00affae0"></a> `00affae0` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00affae4"></a> `00affae4` | `3f 9e eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00affae8"></a> `00affae8` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00affaec"></a> `00affaec` | `73 46 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00affaf0"></a> `00affaf0` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00affaf4"></a> `00affaf4` | `09 ee 80 52` | mov w9,#0x770 | `FALL_THROUGH`
<a id="insn-00affaf8"></a> `00affaf8` | `8a 38 80 52` | mov w10,#0x1c4 | `FALL_THROUGH`
<a id="insn-00affafc"></a> `00affafc` | `bf 02 00 72` | tst w21,#0x1 | `FALL_THROUGH`
<a id="insn-00affb00"></a> `00affb00` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00affb04"></a> `00affb04` | `09 01 09 9b` | madd x9,x8,x9,x0 | `FALL_THROUGH`
<a id="insn-00affb08"></a> `00affb08` | `08 01 0a 9b` | madd x8,x8,x10,x0 | `FALL_THROUGH`
<a id="insn-00affb0c"></a> `00affb0c` | `8a 3b 80 52` | mov w10,#0x1dc | `FALL_THROUGH`
<a id="insn-00affb10"></a> `00affb10` | `69 26 2a 9b` | smaddl x9,w19,w10,x9 | `FALL_THROUGH`
<a id="insn-00affb14"></a> `00affb14` | `29 7d 42 91` | add x9,x9,#0x9f, LSL #12 | `FALL_THROUGH`
<a id="insn-00affb18"></a> `00affb18` | `08 f5 48 91` | add x8,x8,#0x23d, LSL #12 | `FALL_THROUGH`
<a id="insn-00affb1c"></a> `00affb1c` | `29 91 1b 91` | add x9,x9,#0x6e4 | `FALL_THROUGH`
<a id="insn-00affb20"></a> `00affb20` | `08 91 0a 91` | add x8,x8,#0x2a4 | `FALL_THROUGH`
<a id="insn-00affb24"></a> `00affb24` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-00affb28"></a> `00affb28` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00affb2c"></a> `00affb2c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affb30"></a> `00affb30` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affb34"></a> `00affb34` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00affb38"></a> `00affb38` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00affab4`](#insn-00affab4) 範囲 `[['00affab4', '00affae3']]`
  - `FALL_THROUGH` [`00affae0`](#insn-00affae0) → [`00affae4`](#insn-00affae4)
- ブロック [`00affae4`](#insn-00affae4) 範囲 `[['00affae4', '00affaf3']]`
  - `FALL_THROUGH` [`00affaf0`](#insn-00affaf0) → [`00affaf4`](#insn-00affaf4)
- ブロック [`00affaf4`](#insn-00affaf4) 範囲 `[['00affaf4', '00affb07']]`
  - `FALL_THROUGH` [`00affb04`](#insn-00affb04) → [`00affb08`](#insn-00affb08)
- ブロック [`00affb08`](#insn-00affb08) 範囲 `[['00affb08', '00affb0f']]`
  - `FALL_THROUGH` [`00affb0c`](#insn-00affb0c) → [`00affb10`](#insn-00affb10)
- ブロック [`00affb10`](#insn-00affb10) 範囲 `[['00affb10', '00affb13']]`
  - `FALL_THROUGH` [`00affb10`](#insn-00affb10) → [`00affb14`](#insn-00affb14)
- ブロック [`00affb14`](#insn-00affb14) 範囲 `[['00affb14', '00affb17']]`
  - `FALL_THROUGH` [`00affb14`](#insn-00affb14) → [`00affb18`](#insn-00affb18)
- ブロック [`00affb18`](#insn-00affb18) 範囲 `[['00affb18', '00affb3b']]`

## 命令位置別の参照

- [`00affab4`](#insn-00affab4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affab8`](#insn-00affab8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affabc`](#insn-00affabc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affad0`](#insn-00affad0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affae4`](#insn-00affae4) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00affaec`](#insn-00affaec) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00affb28`](#insn-00affb28) → `0023d2a4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00affb2c`](#insn-00affb2c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb30`](#insn-00affb30) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affb34`](#insn-00affb34) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affab4`](#insn-00affab4)

~~~json
{
  "source": "00affab4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affab8`](#insn-00affab8)

~~~json
{
  "source": "00affab8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affabc`](#insn-00affabc)

~~~json
{
  "source": "00affabc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affad0`](#insn-00affad0)

~~~json
{
  "source": "00affad0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affae4`](#insn-00affae4)

~~~json
{
  "source": "00affae4",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affaec`](#insn-00affaec)

~~~json
{
  "source": "00affaec",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affb28`](#insn-00affb28)

~~~json
{
  "source": "00affb28",
  "target": "0023d2a4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6156,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0bab9000000000002040000010000000000000000000000d8bab90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00affb2c`](#insn-00affb2c)

~~~json
{
  "source": "00affb2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb30`](#insn-00affb30)

~~~json
{
  "source": "00affb30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affb34`](#insn-00affb34)

~~~json
{
  "source": "00affb34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
