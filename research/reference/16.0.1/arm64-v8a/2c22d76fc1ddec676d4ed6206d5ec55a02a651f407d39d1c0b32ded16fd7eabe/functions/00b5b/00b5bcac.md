# 00b5bcac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5b884`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5b884.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0008.md#compare-741686b57889054fcc9221b134cbfc0c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b5bd48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bd48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0009.md#compare-fc6af3b04f317629252b965963ae642d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5bcac",
  "name": "_ZN8firebase8callback18CallbackDispatcher11AddCallbackEPNS0_8CallbackE",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df9c576ac2d452adfeaff7332fb85e3283aff6828ce890042412a1dd84b9d4eb",
  "source_text_sha256": "df9c576ac2d452adfeaff7332fb85e3283aff6828ce890042412a1dd84b9d4eb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5bcac",
        "00b5bd93"
      ]
    ],
    "bytes_sha256": "2e1ac4b5ca671182c7f63fd308c6bd7cadf1bdeccb77b3427c1101d49b513e00",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5bb10](../00c5b/00c5bb10.md)

## 呼び出し先

- [00b5c4f4](../00b5c/00b5c4f4.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1529 bytes

~~~c

long * _ZN8firebase8callback18CallbackDispatcher11AddCallbackEPNS0_8CallbackE
                 (long *param_1,long param_2)

{
  char cVar1;
  bool bVar2;
  undefined *puVar3;
  long *plVar4;
  long *plVar5;
  long lVar6;
  long *plVar7;
  long *plVar8;
  
  plVar4 = (long *)_Znwm(0x30);
  plVar4[2] = 0;
  puVar3 = 
  PTR__ZTVNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEEE_00c9b788
  ;
  plVar8 = plVar4 + 1;
  *plVar8 = 0;
  *plVar4 = (long)(puVar3 + 0x10);
  plVar7 = plVar4 + 3;
  *plVar7 = param_2;
  plVar4[4] = (long)(param_1 + 8);
  *(undefined1 *)(plVar4 + 5) = 0;
  _ZN8firebase5Mutex7AcquireEv(param_1 + 3);
  plVar5 = (long *)_Znwm(0x20);
  plVar5[2] = (long)plVar7;
  plVar5[3] = (long)plVar4;
  do {
    cVar1 = '\x01';
    bVar2 = (bool)ExclusiveMonitorPass(plVar8,0x10);
    if (bVar2) {
      *plVar8 = *plVar8 + 1;
      cVar1 = ExclusiveMonitorsStatus();
    }
  } while (cVar1 != '\0');
  lVar6 = *param_1;
  *plVar5 = lVar6;
  plVar5[1] = (long)param_1;
  *(long **)(lVar6 + 8) = plVar5;
  *param_1 = (long)plVar5;
  param_1[2] = param_1[2] + 1;
  _ZN8firebase5Mutex7ReleaseEv(param_1 + 3);
  do {
    lVar6 = *plVar8;
    cVar1 = '\x01';
    bVar2 = (bool)ExclusiveMonitorPass(plVar8,0x10);
    if (bVar2) {
      *plVar8 = lVar6 + -1;
      cVar1 = ExclusiveMonitorsStatus();
    }
  } while (cVar1 != '\0');
  if (lVar6 == 0) {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  return plVar7;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5bcac"></a> `00b5bcac` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00b5bcb0"></a> `00b5bcb0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bcb4"></a> `00b5bcb4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5bcb8"></a> `00b5bcb8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5bcbc"></a> `00b5bcbc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b5bcc0"></a> `00b5bcc0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b5bcc4"></a> `00b5bcc4` | `18 00 01 91` | add x24,x0,#0x40 | `FALL_THROUGH`
<a id="insn-00b5bcc8"></a> `00b5bcc8` | `00 06 80 52` | mov w0,#0x30 | `FALL_THROUGH`
<a id="insn-00b5bccc"></a> `00b5bccc` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00b5bcd0"></a> `00b5bcd0` | `70 f0 03 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00b5bcd4"></a> `00b5bcd4` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bcd8"></a> `00b5bcd8` | `08 0a 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00b5bcdc"></a> `00b5bcdc` | `08 c5 43 f9` | ldr x8,[x8, #0x788] | `FALL_THROUGH`
<a id="insn-00b5bce0"></a> `00b5bce0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00b5bce4"></a> `00b5bce4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b5bce8"></a> `00b5bce8` | `ff 8e 00 f8` | str xzr,[x23, #0x8]! | `FALL_THROUGH`
<a id="insn-00b5bcec"></a> `00b5bcec` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b5bcf0"></a> `00b5bcf0` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5bcf4"></a> `00b5bcf4` | `96 8e 01 f8` | str x22,[x20, #0x18]! | `FALL_THROUGH`
<a id="insn-00b5bcf8"></a> `00b5bcf8` | `b6 62 00 91` | add x22,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00b5bcfc"></a> `00b5bcfc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b5bd00"></a> `00b5bd00` | `18 10 00 f9` | str x24,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00b5bd04"></a> `00b5bd04` | `1f a0 00 39` | strb wzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00b5bd08"></a> `00b5bd08` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b5bd0c"></a> `00b5bd0c` | `3d fb 03 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00b5bd10"></a> `00b5bd10` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00b5bd14"></a> `00b5bd14` | `5f f0 03 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00b5bd18"></a> `00b5bd18` | `14 4c 01 a9` | stp x20,x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bd1c"></a> `00b5bd1c` | `e8 7e 5f c8` | ldxr x8,[x23] | `FALL_THROUGH`
<a id="insn-00b5bd20"></a> `00b5bd20` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5bd24"></a> `00b5bd24` | `e8 7e 09 c8` | stxr w9,x8,[x23] | `FALL_THROUGH`
<a id="insn-00b5bd28"></a> `00b5bd28` | `a9 ff ff 35` | cbnz w9,0x00b5bd1c | `CONDITIONAL_JUMP`
<a id="insn-00b5bd2c"></a> `00b5bd2c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00b5bd30"></a> `00b5bd30` | `08 54 00 a9` | stp x8,x21,[x0] | `FALL_THROUGH`
<a id="insn-00b5bd34"></a> `00b5bd34` | `00 05 00 f9` | str x0,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b5bd38"></a> `00b5bd38` | `a8 0a 40 f9` | ldr x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bd3c"></a> `00b5bd3c` | `a0 02 00 f9` | str x0,[x21] | `FALL_THROUGH`
<a id="insn-00b5bd40"></a> `00b5bd40` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b5bd44"></a> `00b5bd44` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5bd48"></a> `00b5bd48` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bd4c"></a> `00b5bd4c` | `31 fb 03 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00b5bd50"></a> `00b5bd50` | `e8 fe 5f c8` | ldaxr x8,[x23] | `FALL_THROUGH`
<a id="insn-00b5bd54"></a> `00b5bd54` | `09 05 00 d1` | sub x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5bd58"></a> `00b5bd58` | `e9 fe 0a c8` | stlxr w10,x9,[x23] | `FALL_THROUGH`
<a id="insn-00b5bd5c"></a> `00b5bd5c` | `aa ff ff 35` | cbnz w10,0x00b5bd50 | `CONDITIONAL_JUMP`
<a id="insn-00b5bd60"></a> `00b5bd60` | `e8 00 00 b5` | cbnz x8,0x00b5bd7c | `CONDITIONAL_JUMP`
<a id="insn-00b5bd64"></a> `00b5bd64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b5bd68"></a> `00b5bd68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5bd6c"></a> `00b5bd6c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bd70"></a> `00b5bd70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5bd74"></a> `00b5bd74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5bd78"></a> `00b5bd78` | `42 f0 03 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00b5bd7c"></a> `00b5bd7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b5bd80"></a> `00b5bd80` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5bd84"></a> `00b5bd84` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5bd88"></a> `00b5bd88` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bd8c"></a> `00b5bd8c` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b5bd90"></a> `00b5bd90` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5bcac`](#insn-00b5bcac) 範囲 `[['00b5bcac', '00b5bd1b']]`
  - `FALL_THROUGH` [`00b5bd18`](#insn-00b5bd18) → [`00b5bd1c`](#insn-00b5bd1c)
- ブロック [`00b5bd1c`](#insn-00b5bd1c) 範囲 `[['00b5bd1c', '00b5bd2b']]`
  - `CONDITIONAL_JUMP` [`00b5bd28`](#insn-00b5bd28) → [`00b5bd1c`](#insn-00b5bd1c)
  - `FALL_THROUGH` [`00b5bd28`](#insn-00b5bd28) → [`00b5bd2c`](#insn-00b5bd2c)
- ブロック [`00b5bd2c`](#insn-00b5bd2c) 範囲 `[['00b5bd2c', '00b5bd4f']]`
  - `FALL_THROUGH` [`00b5bd4c`](#insn-00b5bd4c) → [`00b5bd50`](#insn-00b5bd50)
- ブロック [`00b5bd50`](#insn-00b5bd50) 範囲 `[['00b5bd50', '00b5bd5f']]`
  - `CONDITIONAL_JUMP` [`00b5bd5c`](#insn-00b5bd5c) → [`00b5bd50`](#insn-00b5bd50)
  - `FALL_THROUGH` [`00b5bd5c`](#insn-00b5bd5c) → [`00b5bd60`](#insn-00b5bd60)
- ブロック [`00b5bd60`](#insn-00b5bd60) 範囲 `[['00b5bd60', '00b5bd63']]`
  - `CONDITIONAL_JUMP` [`00b5bd60`](#insn-00b5bd60) → [`00b5bd7c`](#insn-00b5bd7c)
  - `FALL_THROUGH` [`00b5bd60`](#insn-00b5bd60) → [`00b5bd64`](#insn-00b5bd64)
- ブロック [`00b5bd64`](#insn-00b5bd64) 範囲 `[['00b5bd64', '00b5bd7b']]`
  - `FALL_THROUGH` [`00b5bd78`](#insn-00b5bd78) → [`00b5bd7c`](#insn-00b5bd7c)
- ブロック [`00b5bd7c`](#insn-00b5bd7c) 範囲 `[['00b5bd7c', '00b5bd93']]`

## 命令位置別の参照

- [`00b5bcac`](#insn-00b5bcac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bcb0`](#insn-00b5bcb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bcb4`](#insn-00b5bcb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bcb8`](#insn-00b5bcb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bcd0`](#insn-00b5bcd0) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00b5bcdc`](#insn-00b5bcdc) → `00c9b788`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b5bcf0`](#insn-00b5bcf0) → `00c90318`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[56]`
- [`00b5bd0c`](#insn-00b5bd0c) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd14`](#insn-00b5bd14) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd28`](#insn-00b5bd28) → [`00b5bd1c`](#insn-00b5bd1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd4c`](#insn-00b5bd4c) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd5c`](#insn-00b5bd5c) → [`00b5bd50`](#insn-00b5bd50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd60`](#insn-00b5bd60) → [`00b5bd7c`](#insn-00b5bd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd6c`](#insn-00b5bd6c) → `00c90328`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[56]`
- [`00b5bd70`](#insn-00b5bd70) → [`00b5c4f4`](../00b5c/00b5c4f4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b5c4f4` · 推定シンボル `_ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEE16__on_zero_sharedEv` · 推定型 `None`
- [`00b5bd78`](#insn-00b5bd78) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd80`](#insn-00b5bd80) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd84`](#insn-00b5bd84) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd88`](#insn-00b5bd88) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5bcac`](#insn-00b5bcac)

~~~json
{
  "source": "00b5bcac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bcb0`](#insn-00b5bcb0)

~~~json
{
  "source": "00b5bcb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bcb4`](#insn-00b5bcb4)

~~~json
{
  "source": "00b5bcb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bcb8`](#insn-00b5bcb8)

~~~json
{
  "source": "00b5bcb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bcd0`](#insn-00b5bcd0)

~~~json
{
  "source": "00b5bcd0",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5bcdc`](#insn-00b5bcdc)

~~~json
{
  "source": "00b5bcdc",
  "target": "00c9b788",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b788",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b5bcf0`](#insn-00b5bcf0)

~~~json
{
  "source": "00b5bcf0",
  "target": "00c90318",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90308",
  "offset": 16,
  "size": 56,
  "datatype": "undefined1[56]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00b5bd0c`](#insn-00b5bd0c)

~~~json
{
  "source": "00b5bd0c",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5bd14`](#insn-00b5bd14)

~~~json
{
  "source": "00b5bd14",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5bd28`](#insn-00b5bd28)

~~~json
{
  "source": "00b5bd28",
  "target": "00b5bd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd4c`](#insn-00b5bd4c)

~~~json
{
  "source": "00b5bd4c",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5bd5c`](#insn-00b5bd5c)

~~~json
{
  "source": "00b5bd5c",
  "target": "00b5bd50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd60`](#insn-00b5bd60)

~~~json
{
  "source": "00b5bd60",
  "target": "00b5bd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd6c`](#insn-00b5bd6c)

~~~json
{
  "source": "00b5bd6c",
  "target": "00c90328",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90308",
  "offset": 32,
  "size": 56,
  "datatype": "undefined1[56]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00b5bd70`](#insn-00b5bd70)

~~~json
{
  "source": "00b5bd70",
  "target": "00b5c4f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5bd78`](#insn-00b5bd78)

~~~json
{
  "source": "00b5bd78",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5bd80`](#insn-00b5bd80)

~~~json
{
  "source": "00b5bd80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd84`](#insn-00b5bd84)

~~~json
{
  "source": "00b5bd84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd88`](#insn-00b5bd88)

~~~json
{
  "source": "00b5bd88",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
