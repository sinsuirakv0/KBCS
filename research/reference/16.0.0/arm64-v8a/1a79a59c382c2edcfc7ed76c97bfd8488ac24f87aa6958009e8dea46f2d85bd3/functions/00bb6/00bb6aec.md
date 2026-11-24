# 00bb6aec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b490e4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b490e4.md) · 移動量 `+0x6da08`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0064.md#compare-8c155e0eeffbc70847630a3cdffed6fa)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb6f14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb6/00bb6f14.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0038.md#compare-2e1583fa297773d403dfcfb9f819729b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb6aec",
  "name": "_ZN8firebase9messaging20PollableListenerImpl9OnMessageERKNS0_7MessageE",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1023e5ec752ad74b9278b8ab729820b8bc8109a91d7ac4178345f376c75f73de",
  "source_text_sha256": "1023e5ec752ad74b9278b8ab729820b8bc8109a91d7ac4178345f376c75f73de",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb6aec",
        "00bb6bcb"
      ]
    ],
    "bytes_sha256": "8df6260129d92e2d951170d39da7de001e5cef3f67c1d6c4b68325518e5c1419",
    "instruction_count": 56,
    "instruction_bytes": 224,
    "body_bytes": 224,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5cf70](../00c5c/00c5cf70.md)

## 呼び出し先

- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5cfe0](../00c5c/00c5cfe0.md)
- [00c5cff0](../00c5c/00c5cff0.md)
- [00c5d0b0](../00c5d/00c5d0b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1403 bytes

~~~c

void _ZN8firebase9messaging20PollableListenerImpl9OnMessageERKNS0_7MessageE(long param_1)

{
  ulong uVar1;
  long lVar2;
  long lVar3;
  long lVar4;
  ulong uVar5;
  undefined1 auStack_178 [320];
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  _ZN8firebase9messaging7MessageC2ERKS1_(auStack_178);
  _ZN8firebase5Mutex7AcquireEv(param_1);
  lVar3 = *(long *)(param_1 + 0x78);
  lVar4 = *(long *)(param_1 + 0x80);
  uVar1 = 0;
  if (lVar4 - lVar3 != 0) {
    uVar1 = (lVar4 - lVar3) * 2 - 1;
  }
  uVar5 = *(long *)(param_1 + 0x98) + *(long *)(param_1 + 0x90);
  if (uVar1 == uVar5) {
    _ZNSt6__ndk15dequeIN8firebase9messaging7MessageENS_9allocatorIS3_EEE19__add_back_capacityEv
              (param_1 + 0x70);
    lVar3 = *(long *)(param_1 + 0x78);
    lVar4 = *(long *)(param_1 + 0x80);
    uVar5 = *(long *)(param_1 + 0x90) + *(long *)(param_1 + 0x98);
  }
  if (lVar4 == lVar3) {
    lVar3 = 0;
  }
  else {
    lVar3 = *(long *)(lVar3 + (uVar5 >> 1 & 0x7ffffffffffffff8)) + (uVar5 & 0xf) * 0x140;
  }
  _ZN8firebase9messaging7MessageC2ERKS1_(lVar3,auStack_178);
  *(long *)(param_1 + 0x98) = *(long *)(param_1 + 0x98) + 1;
  _ZN8firebase5Mutex7ReleaseEv(param_1);
  _ZN8firebase9messaging7MessageD2Ev(auStack_178);
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb6aec"></a> `00bb6aec` | `ff 03 06 d1` | sub sp,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bb6af0"></a> `00bb6af0` | `fc ab 00 f9` | str x28,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bb6af4"></a> `00bb6af4` | `f4 4f 16 a9` | stp x20,x19,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00bb6af8"></a> `00bb6af8` | `fd 7b 17 a9` | stp x29,x30,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bb6afc"></a> `00bb6afc` | `fd c3 05 91` | add x29,sp,#0x170 | `FALL_THROUGH`
<a id="insn-00bb6b00"></a> `00bb6b00` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bb6b04"></a> `00bb6b04` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bb6b08"></a> `00bb6b08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb6b0c"></a> `00bb6b0c` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bb6b10"></a> `00bb6b10` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00bb6b14"></a> `00bb6b14` | `33 99 02 94` | bl 0x00c5cfe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6b18"></a> `00bb6b18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb6b1c"></a> `00bb6b1c` | `b9 8e 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6b20"></a> `00bb6b20` | `68 a6 47 a9` | ldp x8,x9,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00bb6b24"></a> `00bb6b24` | `6a 2e 49 a9` | ldp x10,x11,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00bb6b28"></a> `00bb6b28` | `2c 01 08 eb` | subs x12,x9,x8 | `FALL_THROUGH`
<a id="insn-00bb6b2c"></a> `00bb6b2c` | `8c f9 7f d3` | lsl x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6b30"></a> `00bb6b30` | `8c 05 00 d1` | sub x12,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6b34"></a> `00bb6b34` | `ec 03 8c 9a` | csel x12,xzr,x12,eq | `FALL_THROUGH`
<a id="insn-00bb6b38"></a> `00bb6b38` | `6a 01 0a 8b` | add x10,x11,x10 | `FALL_THROUGH`
<a id="insn-00bb6b3c"></a> `00bb6b3c` | `9f 01 0a eb` | cmp x12,x10 | `FALL_THROUGH`
<a id="insn-00bb6b40"></a> `00bb6b40` | `c1 00 00 54` | b.ne 0x00bb6b58 | `CONDITIONAL_JUMP`
<a id="insn-00bb6b44"></a> `00bb6b44` | `60 c2 01 91` | add x0,x19,#0x70 | `FALL_THROUGH`
<a id="insn-00bb6b48"></a> `00bb6b48` | `5a 99 02 94` | bl 0x00c5d0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6b4c"></a> `00bb6b4c` | `6a 2e 49 a9` | ldp x10,x11,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00bb6b50"></a> `00bb6b50` | `68 a6 47 a9` | ldp x8,x9,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00bb6b54"></a> `00bb6b54` | `4a 01 0b 8b` | add x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bb6b58"></a> `00bb6b58` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bb6b5c"></a> `00bb6b5c` | `00 01 00 54` | b.eq 0x00bb6b7c | `CONDITIONAL_JUMP`
<a id="insn-00bb6b60"></a> `00bb6b60` | `49 fd 41 d3` | lsr x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6b64"></a> `00bb6b64` | `29 ed 7d 92` | and x9,x9,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00bb6b68"></a> `00bb6b68` | `08 69 69 f8` | ldr x8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bb6b6c"></a> `00bb6b6c` | `49 0d 40 92` | and x9,x10,#0xf | `FALL_THROUGH`
<a id="insn-00bb6b70"></a> `00bb6b70` | `0a 28 80 52` | mov w10,#0x140 | `FALL_THROUGH`
<a id="insn-00bb6b74"></a> `00bb6b74` | `20 21 0a 9b` | madd x0,x9,x10,x8 | `FALL_THROUGH`
<a id="insn-00bb6b78"></a> `00bb6b78` | `02 00 00 14` | b 0x00bb6b80 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb6b7c"></a> `00bb6b7c` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bb6b80"></a> `00bb6b80` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bb6b84"></a> `00bb6b84` | `17 99 02 94` | bl 0x00c5cfe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6b88"></a> `00bb6b88` | `68 4e 40 f9` | ldr x8,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00bb6b8c"></a> `00bb6b8c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6b90"></a> `00bb6b90` | `68 4e 00 f9` | str x8,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00bb6b94"></a> `00bb6b94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb6b98"></a> `00bb6b98` | `9e 8e 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6b9c"></a> `00bb6b9c` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bb6ba0"></a> `00bb6ba0` | `14 99 02 94` | bl 0x00c5cff0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6ba4"></a> `00bb6ba4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bb6ba8"></a> `00bb6ba8` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00bb6bac"></a> `00bb6bac` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bb6bb0"></a> `00bb6bb0` | `c1 00 00 54` | b.ne 0x00bb6bc8 | `CONDITIONAL_JUMP`
<a id="insn-00bb6bb4"></a> `00bb6bb4` | `fd 7b 57 a9` | ldp x29,x30,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-00bb6bb8"></a> `00bb6bb8` | `f4 4f 56 a9` | ldp x20,x19,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-00bb6bbc"></a> `00bb6bbc` | `fc ab 40 f9` | ldr x28,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-00bb6bc0"></a> `00bb6bc0` | `ff 03 06 91` | add sp,sp,#0x180 | `FALL_THROUGH`
<a id="insn-00bb6bc4"></a> `00bb6bc4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bb6bc8"></a> `00bb6bc8` | `c6 83 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb6aec`](#insn-00bb6aec) 範囲 `[['00bb6aec', '00bb6b43']]`
  - `CONDITIONAL_JUMP` [`00bb6b40`](#insn-00bb6b40) → [`00bb6b58`](#insn-00bb6b58)
  - `FALL_THROUGH` [`00bb6b40`](#insn-00bb6b40) → [`00bb6b44`](#insn-00bb6b44)
- ブロック [`00bb6b44`](#insn-00bb6b44) 範囲 `[['00bb6b44', '00bb6b57']]`
  - `FALL_THROUGH` [`00bb6b54`](#insn-00bb6b54) → [`00bb6b58`](#insn-00bb6b58)
- ブロック [`00bb6b58`](#insn-00bb6b58) 範囲 `[['00bb6b58', '00bb6b5f']]`
  - `CONDITIONAL_JUMP` [`00bb6b5c`](#insn-00bb6b5c) → [`00bb6b7c`](#insn-00bb6b7c)
  - `FALL_THROUGH` [`00bb6b5c`](#insn-00bb6b5c) → [`00bb6b60`](#insn-00bb6b60)
- ブロック [`00bb6b60`](#insn-00bb6b60) 範囲 `[['00bb6b60', '00bb6b7b']]`
  - `UNCONDITIONAL_JUMP` [`00bb6b78`](#insn-00bb6b78) → [`00bb6b80`](#insn-00bb6b80)
- ブロック [`00bb6b7c`](#insn-00bb6b7c) 範囲 `[['00bb6b7c', '00bb6b7f']]`
  - `FALL_THROUGH` [`00bb6b7c`](#insn-00bb6b7c) → [`00bb6b80`](#insn-00bb6b80)
- ブロック [`00bb6b80`](#insn-00bb6b80) 範囲 `[['00bb6b80', '00bb6bb3']]`
  - `CONDITIONAL_JUMP` [`00bb6bb0`](#insn-00bb6bb0) → [`00bb6bc8`](#insn-00bb6bc8)
  - `FALL_THROUGH` [`00bb6bb0`](#insn-00bb6bb0) → [`00bb6bb4`](#insn-00bb6bb4)
- ブロック [`00bb6bb4`](#insn-00bb6bb4) 範囲 `[['00bb6bb4', '00bb6bc7']]`
- ブロック [`00bb6bc8`](#insn-00bb6bc8) 範囲 `[['00bb6bc8', '00bb6bcb']]`

## 命令位置別の参照

- [`00bb6af0`](#insn-00bb6af0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6af4`](#insn-00bb6af4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6af8`](#insn-00bb6af8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6b10`](#insn-00bb6b10) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6b14`](#insn-00bb6b14) → [`00c5cfe0`](../00c5c/00c5cfe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cfe0` · 推定シンボル `None` · 推定型 `None`
- [`00bb6b1c`](#insn-00bb6b1c) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bb6b40`](#insn-00bb6b40) → [`00bb6b58`](#insn-00bb6b58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6b48`](#insn-00bb6b48) → [`00c5d0b0`](../00c5d/00c5d0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bb6b5c`](#insn-00bb6b5c) → [`00bb6b7c`](#insn-00bb6b7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6b78`](#insn-00bb6b78) → [`00bb6b80`](#insn-00bb6b80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6b84`](#insn-00bb6b84) → [`00c5cfe0`](../00c5c/00c5cfe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cfe0` · 推定シンボル `None` · 推定型 `None`
- [`00bb6b98`](#insn-00bb6b98) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bb6ba0`](#insn-00bb6ba0) → [`00c5cff0`](../00c5c/00c5cff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cff0` · 推定シンボル `None` · 推定型 `None`
- [`00bb6ba8`](#insn-00bb6ba8) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6bb0`](#insn-00bb6bb0) → [`00bb6bc8`](#insn-00bb6bc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6bb4`](#insn-00bb6bb4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6bb8`](#insn-00bb6bb8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6bbc`](#insn-00bb6bbc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6bc8`](#insn-00bb6bc8) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb6af0`](#insn-00bb6af0)

~~~json
{
  "source": "00bb6af0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6af4`](#insn-00bb6af4)

~~~json
{
  "source": "00bb6af4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6af8`](#insn-00bb6af8)

~~~json
{
  "source": "00bb6af8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6b10`](#insn-00bb6b10)

~~~json
{
  "source": "00bb6b10",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6b14`](#insn-00bb6b14)

~~~json
{
  "source": "00bb6b14",
  "target": "00c5cfe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6b1c`](#insn-00bb6b1c)

~~~json
{
  "source": "00bb6b1c",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6b40`](#insn-00bb6b40)

~~~json
{
  "source": "00bb6b40",
  "target": "00bb6b58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6b48`](#insn-00bb6b48)

~~~json
{
  "source": "00bb6b48",
  "target": "00c5d0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6b5c`](#insn-00bb6b5c)

~~~json
{
  "source": "00bb6b5c",
  "target": "00bb6b7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6b78`](#insn-00bb6b78)

~~~json
{
  "source": "00bb6b78",
  "target": "00bb6b80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6b84`](#insn-00bb6b84)

~~~json
{
  "source": "00bb6b84",
  "target": "00c5cfe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6b98`](#insn-00bb6b98)

~~~json
{
  "source": "00bb6b98",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6ba0`](#insn-00bb6ba0)

~~~json
{
  "source": "00bb6ba0",
  "target": "00c5cff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6ba8`](#insn-00bb6ba8)

~~~json
{
  "source": "00bb6ba8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6bb0`](#insn-00bb6bb0)

~~~json
{
  "source": "00bb6bb0",
  "target": "00bb6bc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6bb4`](#insn-00bb6bb4)

~~~json
{
  "source": "00bb6bb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6bb8`](#insn-00bb6bb8)

~~~json
{
  "source": "00bb6bb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6bbc`](#insn-00bb6bbc)

~~~json
{
  "source": "00bb6bbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6bc8`](#insn-00bb6bc8)

~~~json
{
  "source": "00bb6bc8",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
