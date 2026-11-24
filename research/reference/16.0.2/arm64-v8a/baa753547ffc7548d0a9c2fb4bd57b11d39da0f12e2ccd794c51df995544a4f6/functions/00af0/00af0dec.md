# 00af0dec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af0d50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0d50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0066.md#compare-cd950f733d56f3aa9db1c322468912db)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00af1de0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00af1/00af1de0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0068.md#compare-46b48ad1bf401ef5223f256829677aa6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af0dec",
  "name": "FUN_00af0dec",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "abe2b46d1199256358f9ff65a5b13a0a8db7a5daf7aa25c4e270580195b55ae4",
  "source_text_sha256": "abe2b46d1199256358f9ff65a5b13a0a8db7a5daf7aa25c4e270580195b55ae4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af0dec",
        "00af0ecf"
      ]
    ],
    "bytes_sha256": "f387b094def0eea54380416bfaf5461f280ac82bcc96a94a16fa7597d36d53f9",
    "instruction_count": 57,
    "instruction_bytes": 228,
    "body_bytes": 228,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00468ca0](../00468/00468ca0.md)
- [00469c44](../00469/00469c44.md)
- [0046d9b4](../0046d/0046d9b4.md)
- [00aea7c0](../00aea/00aea7c0.md)
- [00c586e0](../00c58/00c586e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1243 bytes

~~~c

void FUN_00af0dec(long param_1,undefined8 param_2,undefined8 *param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  long lVar4;
  float fVar5;
  
  lVar4 = *(long *)(param_1 + 8);
  uVar3 = *param_3;
  if (DAT_00ca4a78 == 0) {
    lVar2 = 0;
  }
  else {
                    /* try { // try from 00af0e34 to 00bf0e3b has its CatchHandler @ 00af1018 */
    lVar2 = __dynamic_cast(DAT_00ca4a78,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65f28,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c8da20,0);
  }
  FUN_00aea7c0(lVar4,0);
  FUN_00468ca0(uVar3,5);
  iVar1 = *(int *)((long)&fde_table_entry_00333a38.initial_loc + lVar4);
                    /* try { // try from 00af0e74 to 00bf0e87 has its CatchHandler @ 00af1010 */
  fVar5 = (float)FUN_0046d9b4((float)(*(int *)((long)&fde_table_entry_00336f60.initial_loc + lVar4)
                                     * 0x1e));
                    /* try { // try from 00af0e98 to 00bf0e9f has its CatchHandler @ 00af1020 */
  FUN_00469c44(uVar3,*(undefined8 *)(lVar2 + 0x2d0),(int)((float)(iVar1 + 0x82) + fVar5 * 10.0),
               *(int *)((long)&fde_table_entry_00333a38.data_loc + lVar4) + -6,0x60,0x60,0);
  FUN_00468ca0(uVar3,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af0dec"></a> `00af0dec` | `e8 0f 1c fc` | str d8,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00af0df0"></a> `00af0df0` | `fd fb 00 a9` | stp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00af0df4"></a> `00af0df4` | `f7 0f 00 f9` | str x23,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00af0df8"></a> `00af0df8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af0dfc"></a> `00af0dfc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af0e00"></a> `00af0e00` | `fd 23 00 91` | add x29,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00af0e04"></a> `00af0e04` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00af0e08"></a> `00af0e08` | `a8 0d 00 90` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00af0e0c"></a> `00af0e0c` | `53 00 40 f9` | ldr x19,[x2] | `FALL_THROUGH`
<a id="insn-00af0e10"></a> `00af0e10` | `00 3d 45 f9` | ldr x0,[x8, #0xa78] | `FALL_THROUGH`
<a id="insn-00af0e14"></a> `00af0e14` | `17 ec 8d 52` | mov w23,#0x6f60 | `FALL_THROUGH`
<a id="insn-00af0e18"></a> `00af0e18` | `88 ce 4c 91` | add x8,x20,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-00af0e1c"></a> `00af0e1c` | `77 06 a0 72` | movk w23,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00af0e20"></a> `00af0e20` | `16 e1 28 91` | add x22,x8,#0xa38 | `FALL_THROUGH`
<a id="insn-00af0e24"></a> `00af0e24` | `20 01 00 b4` | cbz x0,0x00af0e48 | `CONDITIONAL_JUMP`
<a id="insn-00af0e28"></a> `00af0e28` | `a1 0b 00 b0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-00af0e2c"></a> `00af0e2c` | `21 a0 3c 91` | add x1,x1,#0xf28 | `FALL_THROUGH`
<a id="insn-00af0e30"></a> `00af0e30` | `e2 0c 00 b0` | adrp x2,0xc8d000 | `FALL_THROUGH`
<a id="insn-00af0e34"></a> `00af0e34` | `42 80 28 91` | add x2,x2,#0xa20 | `FALL_THROUGH`
<a id="insn-00af0e38"></a> `00af0e38` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00af0e3c"></a> `00af0e3c` | `29 9e 05 94` | bl 0x00c586e0 | `UNCONDITIONAL_CALL`
<a id="insn-00af0e40"></a> `00af0e40` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00af0e44"></a> `00af0e44` | `02 00 00 14` | b 0x00af0e4c | `UNCONDITIONAL_JUMP`
<a id="insn-00af0e48"></a> `00af0e48` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00af0e4c"></a> `00af0e4c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00af0e50"></a> `00af0e50` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00af0e54"></a> `00af0e54` | `5b e6 ff 97` | bl 0x00aea7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00af0e58"></a> `00af0e58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af0e5c"></a> `00af0e5c` | `a1 00 80 52` | mov w1,#0x5 | `FALL_THROUGH`
<a id="insn-00af0e60"></a> `00af0e60` | `90 df e5 97` | bl 0x00468ca0 | `UNCONDITIONAL_CALL`
<a id="insn-00af0e64"></a> `00af0e64` | `88 6a 77 b8` | ldr w8,[x20, x23, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af0e68"></a> `00af0e68` | `ca 02 40 b9` | ldr w10,[x22] | `FALL_THROUGH`
<a id="insn-00af0e6c"></a> `00af0e6c` | `09 69 1b 53` | lsl w9,w8,#0x5 | `FALL_THROUGH`
<a id="insn-00af0e70"></a> `00af0e70` | `28 05 08 4b` | sub w8,w9,w8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00af0e74"></a> `00af0e74` | `49 09 02 11` | add w9,w10,#0x82 | `FALL_THROUGH`
<a id="insn-00af0e78"></a> `00af0e78` | `28 01 22 1e` | scvtf s8,w9 | `FALL_THROUGH`
<a id="insn-00af0e7c"></a> `00af0e7c` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-00af0e80"></a> `00af0e80` | `cd f2 e5 97` | bl 0x0046d9b4 | `UNCONDITIONAL_CALL`
<a id="insn-00af0e84"></a> `00af0e84` | `01 90 24 1e` | fmov s1,0x41200000 | `FALL_THROUGH`
<a id="insn-00af0e88"></a> `00af0e88` | `c8 06 40 b9` | ldr w8,[x22, #0x4] | `FALL_THROUGH`
<a id="insn-00af0e8c"></a> `00af0e8c` | `a1 6a 41 f9` | ldr x1,[x21, #0x2d0] | `FALL_THROUGH`
<a id="insn-00af0e90"></a> `00af0e90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af0e94"></a> `00af0e94` | `04 0c 80 52` | mov w4,#0x60 | `FALL_THROUGH`
<a id="insn-00af0e98"></a> `00af0e98` | `05 0c 80 52` | mov w5,#0x60 | `FALL_THROUGH`
<a id="insn-00af0e9c"></a> `00af0e9c` | `03 19 00 51` | sub w3,w8,#0x6 | `FALL_THROUGH`
<a id="insn-00af0ea0"></a> `00af0ea0` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-00af0ea4"></a> `00af0ea4` | `00 20 01 1f` | fmadd s0,s0,s1,s8 | `FALL_THROUGH`
<a id="insn-00af0ea8"></a> `00af0ea8` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-00af0eac"></a> `00af0eac` | `66 e3 e5 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-00af0eb0"></a> `00af0eb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af0eb4"></a> `00af0eb4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00af0eb8"></a> `00af0eb8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af0ebc"></a> `00af0ebc` | `f7 0f 40 f9` | ldr x23,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00af0ec0"></a> `00af0ec0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af0ec4"></a> `00af0ec4` | `fd fb 40 a9` | ldp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00af0ec8"></a> `00af0ec8` | `e8 07 44 fc` | ldr d8,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00af0ecc"></a> `00af0ecc` | `75 df e5 17` | b 0x00468ca0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af0dec`](#insn-00af0dec) 範囲 `[['00af0dec', '00af0e27']]`
  - `CONDITIONAL_JUMP` [`00af0e24`](#insn-00af0e24) → [`00af0e48`](#insn-00af0e48)
  - `FALL_THROUGH` [`00af0e24`](#insn-00af0e24) → [`00af0e28`](#insn-00af0e28)
- ブロック [`00af0e28`](#insn-00af0e28) 範囲 `[['00af0e28', '00af0e33']]`
  - `FALL_THROUGH` [`00af0e30`](#insn-00af0e30) → [`00af0e34`](#insn-00af0e34)
- ブロック [`00af0e34`](#insn-00af0e34) 範囲 `[['00af0e34', '00af0e47']]`
  - `UNCONDITIONAL_JUMP` [`00af0e44`](#insn-00af0e44) → [`00af0e4c`](#insn-00af0e4c)
- ブロック [`00af0e48`](#insn-00af0e48) 範囲 `[['00af0e48', '00af0e4b']]`
  - `FALL_THROUGH` [`00af0e48`](#insn-00af0e48) → [`00af0e4c`](#insn-00af0e4c)
- ブロック [`00af0e4c`](#insn-00af0e4c) 範囲 `[['00af0e4c', '00af0e73']]`
  - `FALL_THROUGH` [`00af0e70`](#insn-00af0e70) → [`00af0e74`](#insn-00af0e74)
- ブロック [`00af0e74`](#insn-00af0e74) 範囲 `[['00af0e74', '00af0e97']]`
  - `FALL_THROUGH` [`00af0e94`](#insn-00af0e94) → [`00af0e98`](#insn-00af0e98)
- ブロック [`00af0e98`](#insn-00af0e98) 範囲 `[['00af0e98', '00af0ecf']]`

## 命令位置別の参照

- [`00af0dec`](#insn-00af0dec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0df0`](#insn-00af0df0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0df4`](#insn-00af0df4) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0df8`](#insn-00af0df8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0dfc`](#insn-00af0dfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0e10`](#insn-00af0e10) → `00ca4a78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00af0e24`](#insn-00af0e24) → [`00af0e48`](#insn-00af0e48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0e2c`](#insn-00af0e2c) → `00c65f28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00af0e34`](#insn-00af0e34) → `00c8da20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`00af0e3c`](#insn-00af0e3c) → [`00c586e0`](../00c58/00c586e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c586e0` · 推定シンボル `None` · 推定型 `None`
- [`00af0e44`](#insn-00af0e44) → [`00af0e4c`](#insn-00af0e4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0e54`](#insn-00af0e54) → [`00aea7c0`](../00aea/00aea7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aea7c0` · 推定シンボル `None` · 推定型 `None`
- [`00af0e60`](#insn-00af0e60) → [`00468ca0`](../00468/00468ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468ca0` · 推定シンボル `None` · 推定型 `None`
- [`00af0e64`](#insn-00af0e64) → `00336f60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00af0e68`](#insn-00af0e68) → `00333a38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00af0e80`](#insn-00af0e80) → [`0046d9b4`](../0046d/0046d9b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d9b4` · 推定シンボル `None` · 推定型 `None`
- [`00af0e88`](#insn-00af0e88) → `00333a3c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00af0eac`](#insn-00af0eac) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`00af0eb8`](#insn-00af0eb8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0ebc`](#insn-00af0ebc) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0ec0`](#insn-00af0ec0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0ec4`](#insn-00af0ec4) → `Stack[-0x38]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af0ecc`](#insn-00af0ecc) → [`00468ca0`](../00468/00468ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468ca0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af0dec`](#insn-00af0dec)

~~~json
{
  "source": "00af0dec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0df0`](#insn-00af0df0)

~~~json
{
  "source": "00af0df0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0df4`](#insn-00af0df4)

~~~json
{
  "source": "00af0df4",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0df8`](#insn-00af0df8)

~~~json
{
  "source": "00af0df8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0dfc`](#insn-00af0dfc)

~~~json
{
  "source": "00af0dfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0e10`](#insn-00af0e10)

~~~json
{
  "source": "00af0e10",
  "target": "00ca4a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4a78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00af0e24`](#insn-00af0e24)

~~~json
{
  "source": "00af0e24",
  "target": "00af0e48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0e2c`](#insn-00af0e2c)

~~~json
{
  "source": "00af0e2c",
  "target": "00c65f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65f28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00af0e34`](#insn-00af0e34)

~~~json
{
  "source": "00af0e34",
  "target": "00c8da20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8da20",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00af0e3c`](#insn-00af0e3c)

~~~json
{
  "source": "00af0e3c",
  "target": "00c586e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0e44`](#insn-00af0e44)

~~~json
{
  "source": "00af0e44",
  "target": "00af0e4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0e54`](#insn-00af0e54)

~~~json
{
  "source": "00af0e54",
  "target": "00aea7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0e60`](#insn-00af0e60)

~~~json
{
  "source": "00af0e60",
  "target": "00468ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0e64`](#insn-00af0e64)

~~~json
{
  "source": "00af0e64",
  "target": "00336f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00336f60",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "3c72780060330a00",
  "capture_start": "00336f60",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00af0e68`](#insn-00af0e68)

~~~json
{
  "source": "00af0e68",
  "target": "00333a38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a38",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "08c36a001c790900",
  "capture_start": "00333a38",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00af0e80`](#insn-00af0e80)

~~~json
{
  "source": "00af0e80",
  "target": "0046d9b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0e88`](#insn-00af0e88)

~~~json
{
  "source": "00af0e88",
  "target": "00333a3c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333a38",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "08c36a001c790900",
  "capture_start": "00333a38",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00af0eac`](#insn-00af0eac)

~~~json
{
  "source": "00af0eac",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af0eb8`](#insn-00af0eb8)

~~~json
{
  "source": "00af0eb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0ebc`](#insn-00af0ebc)

~~~json
{
  "source": "00af0ebc",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0ec0`](#insn-00af0ec0)

~~~json
{
  "source": "00af0ec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0ec4`](#insn-00af0ec4)

~~~json
{
  "source": "00af0ec4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af0ecc`](#insn-00af0ecc)

~~~json
{
  "source": "00af0ecc",
  "target": "00468ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
