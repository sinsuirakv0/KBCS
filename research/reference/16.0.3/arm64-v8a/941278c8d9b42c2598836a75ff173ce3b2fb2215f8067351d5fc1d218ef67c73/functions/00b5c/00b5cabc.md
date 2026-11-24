# 00b5cabc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b5bac8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bac8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0032.md#compare-962cf2ecf7785ea780b20c7e47d627e8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5cabc",
  "name": "_ZN8firebase8callback18CallbackDispatcher14FlushCallbacksEv",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bd90d9d6525f8a9a7b4c96af723892f3b7a7f7c3f7be6411aec9e89ce27d4259",
  "source_text_sha256": "bd90d9d6525f8a9a7b4c96af723892f3b7a7f7c3f7be6411aec9e89ce27d4259",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5cabc",
        "00b5cbc3"
      ]
    ],
    "bytes_sha256": "5aa5474e91c42cb3f1138d671039719ffa3ce161ecd728d37517490acfd5b469",
    "instruction_count": 66,
    "instruction_bytes": 264,
    "body_bytes": 264,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5cbc0](../00c5c/00c5cbc0.md)

## 呼び出し先

- [00c58f20](../00c58/00c58f20.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1894 bytes

~~~c

int _ZN8firebase8callback18CallbackDispatcher14FlushCallbacksEv(long param_1)

{
  long *plVar1;
  char cVar2;
  bool bVar3;
  long lVar4;
  int iVar5;
  long *plVar6;
  long *plVar7;
  
  _ZN8firebase5Mutex7AcquireEv(param_1 + 0x18);
  if (*(long *)(param_1 + 0x10) == 0) {
    iVar5 = 0;
  }
  else {
    iVar5 = 0;
    do {
      lVar4 = *(long *)(param_1 + 8);
      plVar6 = *(long **)(lVar4 + 0x18);
      *(undefined8 *)(lVar4 + 0x10) = 0;
      *(undefined8 *)(lVar4 + 0x18) = 0;
      if (plVar6 != (long *)0x0) {
        plVar7 = plVar6 + 1;
        do {
          lVar4 = *plVar7;
          cVar2 = '\x01';
          bVar3 = (bool)ExclusiveMonitorPass(plVar7,0x10);
          if (bVar3) {
            *plVar7 = lVar4 + -1;
            cVar2 = ExclusiveMonitorsStatus();
          }
        } while (cVar2 != '\0');
        if (lVar4 == 0) {
          (**(code **)(*plVar6 + 0x10))(plVar6);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar6);
        }
      }
      plVar6 = *(long **)(param_1 + 8);
      lVar4 = *plVar6;
      *(long *)(lVar4 + 8) = plVar6[1];
      *(long *)plVar6[1] = lVar4;
      *(long *)(param_1 + 0x10) = *(long *)(param_1 + 0x10) + -1;
      plVar7 = (long *)plVar6[3];
      if (plVar7 != (long *)0x0) {
        plVar1 = plVar7 + 1;
        do {
          lVar4 = *plVar1;
          cVar2 = '\x01';
          bVar3 = (bool)ExclusiveMonitorPass(plVar1,0x10);
          if (bVar3) {
            *plVar1 = lVar4 + -1;
            cVar2 = ExclusiveMonitorsStatus();
          }
        } while (cVar2 != '\0');
        if (lVar4 == 0) {
          (**(code **)(*plVar7 + 0x10))(plVar7);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
        }
      }
      _ZdlPv(plVar6);
      iVar5 = iVar5 + 1;
    } while (*(long *)(param_1 + 0x10) != 0);
  }
  _ZN8firebase5Mutex7ReleaseEv(param_1 + 0x18);
  return iVar5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5cabc"></a> `00b5cabc` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00b5cac0"></a> `00b5cac0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cac4"></a> `00b5cac4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5cac8"></a> `00b5cac8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5cacc"></a> `00b5cacc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b5cad0"></a> `00b5cad0` | `13 60 00 91` | add x19,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00b5cad4"></a> `00b5cad4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b5cad8"></a> `00b5cad8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5cadc"></a> `00b5cadc` | `f1 fb 03 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cae0"></a> `00b5cae0` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cae4"></a> `00b5cae4` | `e8 05 00 b4` | cbz x8,0x00b5cba0 | `CONDITIONAL_JUMP`
<a id="insn-00b5cae8"></a> `00b5cae8` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00b5caec"></a> `00b5caec` | `06 00 00 14` | b 0x00b5cb04 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5caf0"></a> `00b5caf0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b5caf4"></a> `00b5caf4` | `17 f1 03 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00b5caf8"></a> `00b5caf8` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cafc"></a> `00b5cafc` | `b5 06 00 11` | add w21,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00b5cb00"></a> `00b5cb00` | `28 05 00 b4` | cbz x8,0x00b5cba4 | `CONDITIONAL_JUMP`
<a id="insn-00b5cb04"></a> `00b5cb04` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b5cb08"></a> `00b5cb08` | `16 0d 40 f9` | ldr x22,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00b5cb0c"></a> `00b5cb0c` | `1f 7d 01 a9` | stp xzr,xzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cb10"></a> `00b5cb10` | `b6 01 00 b4` | cbz x22,0x00b5cb44 | `CONDITIONAL_JUMP`
<a id="insn-00b5cb14"></a> `00b5cb14` | `c8 22 00 91` | add x8,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00b5cb18"></a> `00b5cb18` | `09 fd 5f c8` | ldaxr x9,[x8] | `FALL_THROUGH`
<a id="insn-00b5cb1c"></a> `00b5cb1c` | `2a 05 00 d1` | sub x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b5cb20"></a> `00b5cb20` | `0a fd 0b c8` | stlxr w11,x10,[x8] | `FALL_THROUGH`
<a id="insn-00b5cb24"></a> `00b5cb24` | `ab ff ff 35` | cbnz w11,0x00b5cb18 | `CONDITIONAL_JUMP`
<a id="insn-00b5cb28"></a> `00b5cb28` | `e9 00 00 b5` | cbnz x9,0x00b5cb44 | `CONDITIONAL_JUMP`
<a id="insn-00b5cb2c"></a> `00b5cb2c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00b5cb30"></a> `00b5cb30` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b5cb34"></a> `00b5cb34` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cb38"></a> `00b5cb38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5cb3c"></a> `00b5cb3c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b5cb40"></a> `00b5cb40` | `f8 f0 03 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cb44"></a> `00b5cb44` | `96 06 40 f9` | ldr x22,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b5cb48"></a> `00b5cb48` | `c8 26 40 a9` | ldp x8,x9,[x22] | `FALL_THROUGH`
<a id="insn-00b5cb4c"></a> `00b5cb4c` | `09 05 00 f9` | str x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b5cb50"></a> `00b5cb50` | `c9 06 40 f9` | ldr x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00b5cb54"></a> `00b5cb54` | `28 01 00 f9` | str x8,[x9] | `FALL_THROUGH`
<a id="insn-00b5cb58"></a> `00b5cb58` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cb5c"></a> `00b5cb5c` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5cb60"></a> `00b5cb60` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cb64"></a> `00b5cb64` | `d7 0e 40 f9` | ldr x23,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00b5cb68"></a> `00b5cb68` | `57 fc ff b4` | cbz x23,0x00b5caf0 | `CONDITIONAL_JUMP`
<a id="insn-00b5cb6c"></a> `00b5cb6c` | `e8 22 00 91` | add x8,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00b5cb70"></a> `00b5cb70` | `09 fd 5f c8` | ldaxr x9,[x8] | `FALL_THROUGH`
<a id="insn-00b5cb74"></a> `00b5cb74` | `2a 05 00 d1` | sub x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b5cb78"></a> `00b5cb78` | `0a fd 0b c8` | stlxr w11,x10,[x8] | `FALL_THROUGH`
<a id="insn-00b5cb7c"></a> `00b5cb7c` | `ab ff ff 35` | cbnz w11,0x00b5cb70 | `CONDITIONAL_JUMP`
<a id="insn-00b5cb80"></a> `00b5cb80` | `89 fb ff b5` | cbnz x9,0x00b5caf0 | `CONDITIONAL_JUMP`
<a id="insn-00b5cb84"></a> `00b5cb84` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00b5cb88"></a> `00b5cb88` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b5cb8c"></a> `00b5cb8c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cb90"></a> `00b5cb90` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5cb94"></a> `00b5cb94` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b5cb98"></a> `00b5cb98` | `e2 f0 03 94` | bl 0x00c58f20 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cb9c"></a> `00b5cb9c` | `d5 ff ff 17` | b 0x00b5caf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5cba0"></a> `00b5cba0` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00b5cba4"></a> `00b5cba4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5cba8"></a> `00b5cba8` | `c2 fb 03 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cbac"></a> `00b5cbac` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00b5cbb0"></a> `00b5cbb0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5cbb4"></a> `00b5cbb4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5cbb8"></a> `00b5cbb8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cbbc"></a> `00b5cbbc` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b5cbc0"></a> `00b5cbc0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5cabc`](#insn-00b5cabc) 範囲 `[['00b5cabc', '00b5cae7']]`
  - `CONDITIONAL_JUMP` [`00b5cae4`](#insn-00b5cae4) → [`00b5cba0`](#insn-00b5cba0)
  - `FALL_THROUGH` [`00b5cae4`](#insn-00b5cae4) → [`00b5cae8`](#insn-00b5cae8)
- ブロック [`00b5cae8`](#insn-00b5cae8) 範囲 `[['00b5cae8', '00b5caef']]`
  - `UNCONDITIONAL_JUMP` [`00b5caec`](#insn-00b5caec) → [`00b5cb04`](#insn-00b5cb04)
- ブロック [`00b5caf0`](#insn-00b5caf0) 範囲 `[['00b5caf0', '00b5cb03']]`
  - `CONDITIONAL_JUMP` [`00b5cb00`](#insn-00b5cb00) → [`00b5cba4`](#insn-00b5cba4)
  - `FALL_THROUGH` [`00b5cb00`](#insn-00b5cb00) → [`00b5cb04`](#insn-00b5cb04)
- ブロック [`00b5cb04`](#insn-00b5cb04) 範囲 `[['00b5cb04', '00b5cb13']]`
  - `CONDITIONAL_JUMP` [`00b5cb10`](#insn-00b5cb10) → [`00b5cb44`](#insn-00b5cb44)
  - `FALL_THROUGH` [`00b5cb10`](#insn-00b5cb10) → [`00b5cb14`](#insn-00b5cb14)
- ブロック [`00b5cb14`](#insn-00b5cb14) 範囲 `[['00b5cb14', '00b5cb17']]`
  - `FALL_THROUGH` [`00b5cb14`](#insn-00b5cb14) → [`00b5cb18`](#insn-00b5cb18)
- ブロック [`00b5cb18`](#insn-00b5cb18) 範囲 `[['00b5cb18', '00b5cb27']]`
  - `CONDITIONAL_JUMP` [`00b5cb24`](#insn-00b5cb24) → [`00b5cb18`](#insn-00b5cb18)
  - `FALL_THROUGH` [`00b5cb24`](#insn-00b5cb24) → [`00b5cb28`](#insn-00b5cb28)
- ブロック [`00b5cb28`](#insn-00b5cb28) 範囲 `[['00b5cb28', '00b5cb2b']]`
  - `CONDITIONAL_JUMP` [`00b5cb28`](#insn-00b5cb28) → [`00b5cb44`](#insn-00b5cb44)
  - `FALL_THROUGH` [`00b5cb28`](#insn-00b5cb28) → [`00b5cb2c`](#insn-00b5cb2c)
- ブロック [`00b5cb2c`](#insn-00b5cb2c) 範囲 `[['00b5cb2c', '00b5cb43']]`
  - `FALL_THROUGH` [`00b5cb40`](#insn-00b5cb40) → [`00b5cb44`](#insn-00b5cb44)
- ブロック [`00b5cb44`](#insn-00b5cb44) 範囲 `[['00b5cb44', '00b5cb6b']]`
  - `CONDITIONAL_JUMP` [`00b5cb68`](#insn-00b5cb68) → [`00b5caf0`](#insn-00b5caf0)
  - `FALL_THROUGH` [`00b5cb68`](#insn-00b5cb68) → [`00b5cb6c`](#insn-00b5cb6c)
- ブロック [`00b5cb6c`](#insn-00b5cb6c) 範囲 `[['00b5cb6c', '00b5cb6f']]`
  - `FALL_THROUGH` [`00b5cb6c`](#insn-00b5cb6c) → [`00b5cb70`](#insn-00b5cb70)
- ブロック [`00b5cb70`](#insn-00b5cb70) 範囲 `[['00b5cb70', '00b5cb7f']]`
  - `CONDITIONAL_JUMP` [`00b5cb7c`](#insn-00b5cb7c) → [`00b5cb70`](#insn-00b5cb70)
  - `FALL_THROUGH` [`00b5cb7c`](#insn-00b5cb7c) → [`00b5cb80`](#insn-00b5cb80)
- ブロック [`00b5cb80`](#insn-00b5cb80) 範囲 `[['00b5cb80', '00b5cb83']]`
  - `CONDITIONAL_JUMP` [`00b5cb80`](#insn-00b5cb80) → [`00b5caf0`](#insn-00b5caf0)
  - `FALL_THROUGH` [`00b5cb80`](#insn-00b5cb80) → [`00b5cb84`](#insn-00b5cb84)
- ブロック [`00b5cb84`](#insn-00b5cb84) 範囲 `[['00b5cb84', '00b5cb9f']]`
  - `UNCONDITIONAL_JUMP` [`00b5cb9c`](#insn-00b5cb9c) → [`00b5caf0`](#insn-00b5caf0)
- ブロック [`00b5cba0`](#insn-00b5cba0) 範囲 `[['00b5cba0', '00b5cba3']]`
  - `FALL_THROUGH` [`00b5cba0`](#insn-00b5cba0) → [`00b5cba4`](#insn-00b5cba4)
- ブロック [`00b5cba4`](#insn-00b5cba4) 範囲 `[['00b5cba4', '00b5cbc3']]`

## 命令位置別の参照

- [`00b5cabc`](#insn-00b5cabc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cac0`](#insn-00b5cac0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cac4`](#insn-00b5cac4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cac8`](#insn-00b5cac8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cadc`](#insn-00b5cadc) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00b5cae4`](#insn-00b5cae4) → [`00b5cba0`](#insn-00b5cba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5caec`](#insn-00b5caec) → [`00b5cb04`](#insn-00b5cb04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5caf4`](#insn-00b5caf4) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00b5cb00`](#insn-00b5cb00) → [`00b5cba4`](#insn-00b5cba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cb10`](#insn-00b5cb10) → [`00b5cb44`](#insn-00b5cb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cb24`](#insn-00b5cb24) → [`00b5cb18`](#insn-00b5cb18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cb28`](#insn-00b5cb28) → [`00b5cb44`](#insn-00b5cb44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cb40`](#insn-00b5cb40) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00b5cb68`](#insn-00b5cb68) → [`00b5caf0`](#insn-00b5caf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cb7c`](#insn-00b5cb7c) → [`00b5cb70`](#insn-00b5cb70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cb80`](#insn-00b5cb80) → [`00b5caf0`](#insn-00b5caf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cb98`](#insn-00b5cb98) → [`00c58f20`](../00c58/00c58f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f20` · 推定シンボル `None` · 推定型 `None`
- [`00b5cb9c`](#insn-00b5cb9c) → [`00b5caf0`](#insn-00b5caf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cba8`](#insn-00b5cba8) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00b5cbb0`](#insn-00b5cbb0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cbb4`](#insn-00b5cbb4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cbb8`](#insn-00b5cbb8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5cabc`](#insn-00b5cabc)

~~~json
{
  "source": "00b5cabc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cac0`](#insn-00b5cac0)

~~~json
{
  "source": "00b5cac0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cac4`](#insn-00b5cac4)

~~~json
{
  "source": "00b5cac4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cac8`](#insn-00b5cac8)

~~~json
{
  "source": "00b5cac8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cadc`](#insn-00b5cadc)

~~~json
{
  "source": "00b5cadc",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cae4`](#insn-00b5cae4)

~~~json
{
  "source": "00b5cae4",
  "target": "00b5cba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5caec`](#insn-00b5caec)

~~~json
{
  "source": "00b5caec",
  "target": "00b5cb04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5caf4`](#insn-00b5caf4)

~~~json
{
  "source": "00b5caf4",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cb00`](#insn-00b5cb00)

~~~json
{
  "source": "00b5cb00",
  "target": "00b5cba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cb10`](#insn-00b5cb10)

~~~json
{
  "source": "00b5cb10",
  "target": "00b5cb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cb24`](#insn-00b5cb24)

~~~json
{
  "source": "00b5cb24",
  "target": "00b5cb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cb28`](#insn-00b5cb28)

~~~json
{
  "source": "00b5cb28",
  "target": "00b5cb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cb40`](#insn-00b5cb40)

~~~json
{
  "source": "00b5cb40",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cb68`](#insn-00b5cb68)

~~~json
{
  "source": "00b5cb68",
  "target": "00b5caf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cb7c`](#insn-00b5cb7c)

~~~json
{
  "source": "00b5cb7c",
  "target": "00b5cb70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cb80`](#insn-00b5cb80)

~~~json
{
  "source": "00b5cb80",
  "target": "00b5caf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cb98`](#insn-00b5cb98)

~~~json
{
  "source": "00b5cb98",
  "target": "00c58f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cb9c`](#insn-00b5cb9c)

~~~json
{
  "source": "00b5cb9c",
  "target": "00b5caf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cba8`](#insn-00b5cba8)

~~~json
{
  "source": "00b5cba8",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cbb0`](#insn-00b5cbb0)

~~~json
{
  "source": "00b5cbb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cbb4`](#insn-00b5cbb4)

~~~json
{
  "source": "00b5cbb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cbb8`](#insn-00b5cbb8)

~~~json
{
  "source": "00b5cbb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
