# 00bb6dfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bb69d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb69d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0038.md#compare-58f06c77bffdb782946978a8e8e88ed9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bb6e98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-a08d57c442b6a77b0ee2a91754e0e4bd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb6dfc",
  "name": "_ZN8firebase9messaging20PollableListenerImplD2Ev",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f96052cd26fa01dc0141841a55a15085ff204f83b468cec7303ea8c800b32d88",
  "source_text_sha256": "f96052cd26fa01dc0141841a55a15085ff204f83b468cec7303ea8c800b32d88",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb6dfc",
        "00bb6ebb"
      ]
    ],
    "bytes_sha256": "8c822df311599c08e9fcd40275fa7eb0eb4a0bba712ddf96ca51a4b3ae49e208",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d380](../00c5d/00c5d380.md)

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5aaa0](../00c5a/00c5aaa0.md)
- [00c5d460](../00c5d/00c5d460.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1349 bytes

~~~c

void _ZN8firebase9messaging20PollableListenerImplD2Ev(long param_1)

{
  undefined8 *puVar1;
  byte bVar2;
  long lVar3;
  void *__ptr;
  undefined8 *puVar4;
  undefined8 *puVar5;
  
  _ZNSt6__ndk112__deque_baseIN8firebase9messaging7MessageENS_9allocatorIS3_EEE5clearEv
            ((undefined8 *)(param_1 + 0x70));
  puVar1 = *(undefined8 **)(param_1 + 0x80);
  puVar4 = *(undefined8 **)(param_1 + 0x78);
  if (*(undefined8 **)(param_1 + 0x78) != puVar1) {
    do {
      puVar5 = puVar4 + 1;
      _ZdlPv((void *)*puVar4);
      puVar4 = puVar5;
    } while (puVar1 != puVar5);
    lVar3 = *(long *)(param_1 + 0x80) - *(long *)(param_1 + 0x78);
    if (lVar3 != 0) {
      *(ulong *)(param_1 + 0x80) =
           *(long *)(param_1 + 0x80) + (lVar3 - 8U >> 3 ^ 0xffffffffffffffff) * 8;
    }
  }
  __ptr = *(void **)(param_1 + 0x70);
  if (__ptr != (void *)0x0) {
    _ZdlPv(__ptr);
  }
  if ((*(byte *)(param_1 + 0x58) & 1) == 0) {
    bVar2 = *(byte *)(param_1 + 0x40);
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x68));
    bVar2 = *(byte *)(param_1 + 0x40);
  }
  if ((bVar2 & 1) == 0) {
    bVar2 = *(byte *)(param_1 + 0x28);
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x50));
    bVar2 = *(byte *)(param_1 + 0x28);
  }
  if ((bVar2 & 1) != 0) {
    _ZdlPv(*(void **)(param_1 + 0x38));
  }
  _ZN8firebase5MutexD1Ev(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb6dfc"></a> `00bb6dfc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bb6e00"></a> `00bb6e00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb6e04"></a> `00bb6e04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb6e08"></a> `00bb6e08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bb6e0c"></a> `00bb6e0c` | `14 c0 01 91` | add x20,x0,#0x70 | `FALL_THROUGH`
<a id="insn-00bb6e10"></a> `00bb6e10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb6e14"></a> `00bb6e14` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bb6e18"></a> `00bb6e18` | `92 99 02 94` | bl 0x00c5d460 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6e1c"></a> `00bb6e1c` | `75 da 47 a9` | ldp x21,x22,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00bb6e20"></a> `00bb6e20` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-00bb6e24"></a> `00bb6e24` | `a0 01 00 54` | b.eq 0x00bb6e58 | `CONDITIONAL_JUMP`
<a id="insn-00bb6e28"></a> `00bb6e28` | `a0 86 40 f8` | ldr x0,[x21], #0x8 | `FALL_THROUGH`
<a id="insn-00bb6e2c"></a> `00bb6e2c` | `21 84 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6e30"></a> `00bb6e30` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00bb6e34"></a> `00bb6e34` | `a1 ff ff 54` | b.ne 0x00bb6e28 | `CONDITIONAL_JUMP`
<a id="insn-00bb6e38"></a> `00bb6e38` | `69 a2 47 a9` | ldp x9,x8,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00bb6e3c"></a> `00bb6e3c` | `09 01 09 eb` | subs x9,x8,x9 | `FALL_THROUGH`
<a id="insn-00bb6e40"></a> `00bb6e40` | `c0 00 00 54` | b.eq 0x00bb6e58 | `CONDITIONAL_JUMP`
<a id="insn-00bb6e44"></a> `00bb6e44` | `29 21 00 d1` | sub x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bb6e48"></a> `00bb6e48` | `0a 00 80 92` | mov x10,#-0x1 | `FALL_THROUGH`
<a id="insn-00bb6e4c"></a> `00bb6e4c` | `49 0d 49 ca` | eor x9,x10,x9, LSR #0x3 | `FALL_THROUGH`
<a id="insn-00bb6e50"></a> `00bb6e50` | `08 0d 09 8b` | add x8,x8,x9, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bb6e54"></a> `00bb6e54` | `68 42 00 f9` | str x8,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bb6e58"></a> `00bb6e58` | `80 02 40 f9` | ldr x0,[x20] | `FALL_THROUGH`
<a id="insn-00bb6e5c"></a> `00bb6e5c` | `40 00 00 b4` | cbz x0,0x00bb6e64 | `CONDITIONAL_JUMP`
<a id="insn-00bb6e60"></a> `00bb6e60` | `14 84 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6e64"></a> `00bb6e64` | `68 62 41 39` | ldrb w8,[x19, #0x58] | `FALL_THROUGH`
<a id="insn-00bb6e68"></a> `00bb6e68` | `88 01 00 37` | tbnz w8,#0x0,0x00bb6e98 | `CONDITIONAL_JUMP`
<a id="insn-00bb6e6c"></a> `00bb6e6c` | `68 02 41 39` | ldrb w8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00bb6e70"></a> `00bb6e70` | `c8 01 00 37` | tbnz w8,#0x0,0x00bb6ea8 | `CONDITIONAL_JUMP`
<a id="insn-00bb6e74"></a> `00bb6e74` | `68 a2 40 39` | ldrb w8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bb6e78"></a> `00bb6e78` | `68 00 00 36` | tbz w8,#0x0,0x00bb6e84 | `CONDITIONAL_JUMP`
<a id="insn-00bb6e7c"></a> `00bb6e7c` | `60 1e 40 f9` | ldr x0,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00bb6e80"></a> `00bb6e80` | `0c 84 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6e84"></a> `00bb6e84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb6e88"></a> `00bb6e88` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb6e8c"></a> `00bb6e8c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb6e90"></a> `00bb6e90` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bb6e94"></a> `00bb6e94` | `03 8f 02 14` | b 0x00c5aaa0 | `CALL_TERMINATOR`
<a id="insn-00bb6e98"></a> `00bb6e98` | `60 36 40 f9` | ldr x0,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00bb6e9c"></a> `00bb6e9c` | `05 84 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6ea0"></a> `00bb6ea0` | `68 02 41 39` | ldrb w8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00bb6ea4"></a> `00bb6ea4` | `88 fe 07 36` | tbz w8,#0x0,0x00bb6e74 | `CONDITIONAL_JUMP`
<a id="insn-00bb6ea8"></a> `00bb6ea8` | `60 2a 40 f9` | ldr x0,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00bb6eac"></a> `00bb6eac` | `01 84 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6eb0"></a> `00bb6eb0` | `68 a2 40 39` | ldrb w8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00bb6eb4"></a> `00bb6eb4` | `48 fe 07 37` | tbnz w8,#0x0,0x00bb6e7c | `CONDITIONAL_JUMP`
<a id="insn-00bb6eb8"></a> `00bb6eb8` | `f3 ff ff 17` | b 0x00bb6e84 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bb6dfc`](#insn-00bb6dfc) 範囲 `[['00bb6dfc', '00bb6e27']]`
  - `CONDITIONAL_JUMP` [`00bb6e24`](#insn-00bb6e24) → [`00bb6e58`](#insn-00bb6e58)
  - `FALL_THROUGH` [`00bb6e24`](#insn-00bb6e24) → [`00bb6e28`](#insn-00bb6e28)
- ブロック [`00bb6e28`](#insn-00bb6e28) 範囲 `[['00bb6e28', '00bb6e37']]`
  - `CONDITIONAL_JUMP` [`00bb6e34`](#insn-00bb6e34) → [`00bb6e28`](#insn-00bb6e28)
  - `FALL_THROUGH` [`00bb6e34`](#insn-00bb6e34) → [`00bb6e38`](#insn-00bb6e38)
- ブロック [`00bb6e38`](#insn-00bb6e38) 範囲 `[['00bb6e38', '00bb6e43']]`
  - `CONDITIONAL_JUMP` [`00bb6e40`](#insn-00bb6e40) → [`00bb6e58`](#insn-00bb6e58)
  - `FALL_THROUGH` [`00bb6e40`](#insn-00bb6e40) → [`00bb6e44`](#insn-00bb6e44)
- ブロック [`00bb6e44`](#insn-00bb6e44) 範囲 `[['00bb6e44', '00bb6e57']]`
  - `FALL_THROUGH` [`00bb6e54`](#insn-00bb6e54) → [`00bb6e58`](#insn-00bb6e58)
- ブロック [`00bb6e58`](#insn-00bb6e58) 範囲 `[['00bb6e58', '00bb6e5f']]`
  - `CONDITIONAL_JUMP` [`00bb6e5c`](#insn-00bb6e5c) → [`00bb6e64`](#insn-00bb6e64)
  - `FALL_THROUGH` [`00bb6e5c`](#insn-00bb6e5c) → [`00bb6e60`](#insn-00bb6e60)
- ブロック [`00bb6e60`](#insn-00bb6e60) 範囲 `[['00bb6e60', '00bb6e63']]`
  - `FALL_THROUGH` [`00bb6e60`](#insn-00bb6e60) → [`00bb6e64`](#insn-00bb6e64)
- ブロック [`00bb6e64`](#insn-00bb6e64) 範囲 `[['00bb6e64', '00bb6e6b']]`
  - `CONDITIONAL_JUMP` [`00bb6e68`](#insn-00bb6e68) → [`00bb6e98`](#insn-00bb6e98)
  - `FALL_THROUGH` [`00bb6e68`](#insn-00bb6e68) → [`00bb6e6c`](#insn-00bb6e6c)
- ブロック [`00bb6e6c`](#insn-00bb6e6c) 範囲 `[['00bb6e6c', '00bb6e73']]`
  - `CONDITIONAL_JUMP` [`00bb6e70`](#insn-00bb6e70) → [`00bb6ea8`](#insn-00bb6ea8)
  - `FALL_THROUGH` [`00bb6e70`](#insn-00bb6e70) → [`00bb6e74`](#insn-00bb6e74)
- ブロック [`00bb6e74`](#insn-00bb6e74) 範囲 `[['00bb6e74', '00bb6e7b']]`
  - `CONDITIONAL_JUMP` [`00bb6e78`](#insn-00bb6e78) → [`00bb6e84`](#insn-00bb6e84)
  - `FALL_THROUGH` [`00bb6e78`](#insn-00bb6e78) → [`00bb6e7c`](#insn-00bb6e7c)
- ブロック [`00bb6e7c`](#insn-00bb6e7c) 範囲 `[['00bb6e7c', '00bb6e83']]`
  - `FALL_THROUGH` [`00bb6e80`](#insn-00bb6e80) → [`00bb6e84`](#insn-00bb6e84)
- ブロック [`00bb6e84`](#insn-00bb6e84) 範囲 `[['00bb6e84', '00bb6e97']]`
- ブロック [`00bb6e98`](#insn-00bb6e98) 範囲 `[['00bb6e98', '00bb6ea7']]`
  - `CONDITIONAL_JUMP` [`00bb6ea4`](#insn-00bb6ea4) → [`00bb6e74`](#insn-00bb6e74)
  - `FALL_THROUGH` [`00bb6ea4`](#insn-00bb6ea4) → [`00bb6ea8`](#insn-00bb6ea8)
- ブロック [`00bb6ea8`](#insn-00bb6ea8) 範囲 `[['00bb6ea8', '00bb6eb7']]`
  - `CONDITIONAL_JUMP` [`00bb6eb4`](#insn-00bb6eb4) → [`00bb6e7c`](#insn-00bb6e7c)
  - `FALL_THROUGH` [`00bb6eb4`](#insn-00bb6eb4) → [`00bb6eb8`](#insn-00bb6eb8)
- ブロック [`00bb6eb8`](#insn-00bb6eb8) 範囲 `[['00bb6eb8', '00bb6ebb']]`
  - `UNCONDITIONAL_JUMP` [`00bb6eb8`](#insn-00bb6eb8) → [`00bb6e84`](#insn-00bb6e84)

## 命令位置別の参照

- [`00bb6dfc`](#insn-00bb6dfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e00`](#insn-00bb6e00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e04`](#insn-00bb6e04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e18`](#insn-00bb6e18) → [`00c5d460`](../00c5d/00c5d460.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d460` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e24`](#insn-00bb6e24) → [`00bb6e58`](#insn-00bb6e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e2c`](#insn-00bb6e2c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e34`](#insn-00bb6e34) → [`00bb6e28`](#insn-00bb6e28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e40`](#insn-00bb6e40) → [`00bb6e58`](#insn-00bb6e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e5c`](#insn-00bb6e5c) → [`00bb6e64`](#insn-00bb6e64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e60`](#insn-00bb6e60) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e68`](#insn-00bb6e68) → [`00bb6e98`](#insn-00bb6e98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e70`](#insn-00bb6e70) → [`00bb6ea8`](#insn-00bb6ea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e78`](#insn-00bb6e78) → [`00bb6e84`](#insn-00bb6e84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e80`](#insn-00bb6e80) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e88`](#insn-00bb6e88) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e8c`](#insn-00bb6e8c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e94`](#insn-00bb6e94) → [`00c5aaa0`](../00c5a/00c5aaa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aaa0` · 推定シンボル `None` · 推定型 `None`
- [`00bb6e9c`](#insn-00bb6e9c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bb6ea4`](#insn-00bb6ea4) → [`00bb6e74`](#insn-00bb6e74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6eac`](#insn-00bb6eac) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bb6eb4`](#insn-00bb6eb4) → [`00bb6e7c`](#insn-00bb6e7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6eb8`](#insn-00bb6eb8) → [`00bb6e84`](#insn-00bb6e84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb6dfc`](#insn-00bb6dfc)

~~~json
{
  "source": "00bb6dfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6e00`](#insn-00bb6e00)

~~~json
{
  "source": "00bb6e00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6e04`](#insn-00bb6e04)

~~~json
{
  "source": "00bb6e04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6e18`](#insn-00bb6e18)

~~~json
{
  "source": "00bb6e18",
  "target": "00c5d460",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6e24`](#insn-00bb6e24)

~~~json
{
  "source": "00bb6e24",
  "target": "00bb6e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6e2c`](#insn-00bb6e2c)

~~~json
{
  "source": "00bb6e2c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6e34`](#insn-00bb6e34)

~~~json
{
  "source": "00bb6e34",
  "target": "00bb6e28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6e40`](#insn-00bb6e40)

~~~json
{
  "source": "00bb6e40",
  "target": "00bb6e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6e5c`](#insn-00bb6e5c)

~~~json
{
  "source": "00bb6e5c",
  "target": "00bb6e64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6e60`](#insn-00bb6e60)

~~~json
{
  "source": "00bb6e60",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6e68`](#insn-00bb6e68)

~~~json
{
  "source": "00bb6e68",
  "target": "00bb6e98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6e70`](#insn-00bb6e70)

~~~json
{
  "source": "00bb6e70",
  "target": "00bb6ea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6e78`](#insn-00bb6e78)

~~~json
{
  "source": "00bb6e78",
  "target": "00bb6e84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6e80`](#insn-00bb6e80)

~~~json
{
  "source": "00bb6e80",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6e88`](#insn-00bb6e88)

~~~json
{
  "source": "00bb6e88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6e8c`](#insn-00bb6e8c)

~~~json
{
  "source": "00bb6e8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6e94`](#insn-00bb6e94)

~~~json
{
  "source": "00bb6e94",
  "target": "00c5aaa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6e9c`](#insn-00bb6e9c)

~~~json
{
  "source": "00bb6e9c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6ea4`](#insn-00bb6ea4)

~~~json
{
  "source": "00bb6ea4",
  "target": "00bb6e74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6eac`](#insn-00bb6eac)

~~~json
{
  "source": "00bb6eac",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6eb4`](#insn-00bb6eb4)

~~~json
{
  "source": "00bb6eb4",
  "target": "00bb6e7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6eb8`](#insn-00bb6eb8)

~~~json
{
  "source": "00bb6eb8",
  "target": "00bb6e84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
