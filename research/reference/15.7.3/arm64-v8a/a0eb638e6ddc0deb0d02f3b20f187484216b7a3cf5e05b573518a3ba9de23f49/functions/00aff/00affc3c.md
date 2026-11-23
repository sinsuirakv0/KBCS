# 00affc3c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00affb74`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aff/00affb74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-760ef3616434720dd9c1815616824cba)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00affc80`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aff/00affc80.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-f1cc65522ddb4a3a66ed4e9379c8d5a3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00affc3c",
  "name": "_ZNK8firebase26ReferenceCountedFutureImpl15GetFutureResultERKNS_12FutureHandleE",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5cf7e34a2b03af1619d882079982a7671ab4f0d5d42ecf57adaa854b5fce0ba3",
  "source_text_sha256": "5cf7e34a2b03af1619d882079982a7671ab4f0d5d42ecf57adaa854b5fce0ba3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00affc3c",
        "00affceb"
      ]
    ],
    "bytes_sha256": "60d482304d2901b4ae8cf2b82cb68b12e89e59b2090e8ddd0fb3de5cf318e231",
    "instruction_count": 44,
    "instruction_bytes": 176,
    "body_bytes": 176,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1913 bytes

~~~c

undefined8
_ZNK8firebase26ReferenceCountedFutureImpl15GetFutureResultERKNS_12FutureHandleE
          (long param_1,ulong *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long *plVar4;
  undefined8 uVar5;
  int *piVar6;
  ulong uVar7;
  
                    /* catch() { ... } // from try @ 00af5be0 with catch @ 00affc44 */
  lVar1 = param_1 + 8;
                    /* catch() { ... } // from try @ 00af5bd4 with catch @ 00affc50 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  uVar7 = *param_2;
                    /* catch() { ... } // from try @ 00af5bc8 with catch @ 00affc68 */
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  plVar4 = (long *)(param_1 + 0x38);
  plVar3 = (long *)*plVar4;
  plVar2 = plVar4;
  if (plVar3 == (long *)0x0) {
LAB_00affca4:
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  else {
    do {
      if ((ulong)plVar3[4] >= uVar7) {
        plVar2 = plVar3;
      }
      plVar3 = (long *)plVar3[(ulong)plVar3[4] < uVar7];
                    /* catch() { ... } // from try @ 00af5bb0 with catch @ 00affc8c */
    } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00af5ba4 with catch @ 00affc98 */
    if ((plVar2 == plVar4) || (uVar7 < (ulong)plVar2[4])) goto LAB_00affca4;
    piVar6 = (int *)plVar2[5];
                    /* catch() { ... } // from try @ 00af5b80 with catch @ 00affcd4 */
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
    uVar5 = 0;
    if (piVar6 == (int *)0x0) goto LAB_00affcb0;
                    /* catch() { ... } // from try @ 00af5b50 with catch @ 00affce0 */
    if (*piVar6 == 0) {
      uVar5 = *(undefined8 *)(piVar6 + 10);
      goto LAB_00affcb0;
    }
  }
  uVar5 = 0;
LAB_00affcb0:
                    /* catch() { ... } // from try @ 00af5b98 with catch @ 00affcb0 */
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
                    /* catch() { ... } // from try @ 00af5b8c with catch @ 00affcbc */
  return uVar5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00affc3c"></a> `00affc3c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00affc40"></a> `00affc40` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affc44"></a> `00affc44` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affc48"></a> `00affc48` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00affc4c"></a> `00affc4c` | `13 20 00 91` | add x19,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00affc50"></a> `00affc50` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00affc54"></a> `00affc54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affc58"></a> `00affc58` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00affc5c"></a> `00affc5c` | `dd 77 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00affc60"></a> `00affc60` | `b5 02 40 f9` | ldr x21,[x21] | `FALL_THROUGH`
<a id="insn-00affc64"></a> `00affc64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affc68"></a> `00affc68` | `da 77 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00affc6c"></a> `00affc6c` | `89 8e 43 f8` | ldr x9,[x20, #0x38]! | `FALL_THROUGH`
<a id="insn-00affc70"></a> `00affc70` | `a9 01 00 b4` | cbz x9,0x00affca4 | `CONDITIONAL_JUMP`
<a id="insn-00affc74"></a> `00affc74` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00affc78"></a> `00affc78` | `2a 11 40 f9` | ldr x10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00affc7c"></a> `00affc7c` | `5f 01 15 eb` | cmp x10,x21 | `FALL_THROUGH`
<a id="insn-00affc80"></a> `00affc80` | `ea 27 9f 1a` | cset w10,cc | `FALL_THROUGH`
<a id="insn-00affc84"></a> `00affc84` | `08 31 89 9a` | csel x8,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00affc88"></a> `00affc88` | `29 59 6a f8` | ldr x9,[x9, w10, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00affc8c"></a> `00affc8c` | `69 ff ff b5` | cbnz x9,0x00affc78 | `CONDITIONAL_JUMP`
<a id="insn-00affc90"></a> `00affc90` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00affc94"></a> `00affc94` | `80 00 00 54` | b.eq 0x00affca4 | `CONDITIONAL_JUMP`
<a id="insn-00affc98"></a> `00affc98` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00affc9c"></a> `00affc9c` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00affca0"></a> `00affca0` | `69 01 00 54` | b.ls 0x00affccc | `CONDITIONAL_JUMP`
<a id="insn-00affca4"></a> `00affca4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affca8"></a> `00affca8` | `ce 77 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affcac"></a> `00affcac` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00affcb0"></a> `00affcb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affcb4"></a> `00affcb4` | `cb 77 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affcb8"></a> `00affcb8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00affcbc"></a> `00affcbc` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00affcc0"></a> `00affcc0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00affcc4"></a> `00affcc4` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00affcc8"></a> `00affcc8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00affccc"></a> `00affccc` | `14 15 40 f9` | ldr x20,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00affcd0"></a> `00affcd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00affcd4"></a> `00affcd4` | `c3 77 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00affcd8"></a> `00affcd8` | `d4 fe ff b4` | cbz x20,0x00affcb0 | `CONDITIONAL_JUMP`
<a id="insn-00affcdc"></a> `00affcdc` | `88 02 40 b9` | ldr w8,[x20] | `FALL_THROUGH`
<a id="insn-00affce0"></a> `00affce0` | `68 fe ff 35` | cbnz w8,0x00affcac | `CONDITIONAL_JUMP`
<a id="insn-00affce4"></a> `00affce4` | `94 16 40 f9` | ldr x20,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00affce8"></a> `00affce8` | `f2 ff ff 17` | b 0x00affcb0 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00affc3c`](#insn-00affc3c) 範囲 `[['00affc3c', '00affc43']]`
  - `FALL_THROUGH` [`00affc40`](#insn-00affc40) → [`00affc44`](#insn-00affc44)
- ブロック [`00affc44`](#insn-00affc44) 範囲 `[['00affc44', '00affc4f']]`
  - `FALL_THROUGH` [`00affc4c`](#insn-00affc4c) → [`00affc50`](#insn-00affc50)
- ブロック [`00affc50`](#insn-00affc50) 範囲 `[['00affc50', '00affc67']]`
  - `FALL_THROUGH` [`00affc64`](#insn-00affc64) → [`00affc68`](#insn-00affc68)
- ブロック [`00affc68`](#insn-00affc68) 範囲 `[['00affc68', '00affc73']]`
  - `CONDITIONAL_JUMP` [`00affc70`](#insn-00affc70) → [`00affca4`](#insn-00affca4)
  - `FALL_THROUGH` [`00affc70`](#insn-00affc70) → [`00affc74`](#insn-00affc74)
- ブロック [`00affc74`](#insn-00affc74) 範囲 `[['00affc74', '00affc77']]`
  - `FALL_THROUGH` [`00affc74`](#insn-00affc74) → [`00affc78`](#insn-00affc78)
- ブロック [`00affc78`](#insn-00affc78) 範囲 `[['00affc78', '00affc8b']]`
  - `FALL_THROUGH` [`00affc88`](#insn-00affc88) → [`00affc8c`](#insn-00affc8c)
- ブロック [`00affc8c`](#insn-00affc8c) 範囲 `[['00affc8c', '00affc8f']]`
  - `CONDITIONAL_JUMP` [`00affc8c`](#insn-00affc8c) → [`00affc78`](#insn-00affc78)
  - `FALL_THROUGH` [`00affc8c`](#insn-00affc8c) → [`00affc90`](#insn-00affc90)
- ブロック [`00affc90`](#insn-00affc90) 範囲 `[['00affc90', '00affc97']]`
  - `CONDITIONAL_JUMP` [`00affc94`](#insn-00affc94) → [`00affca4`](#insn-00affca4)
  - `FALL_THROUGH` [`00affc94`](#insn-00affc94) → [`00affc98`](#insn-00affc98)
- ブロック [`00affc98`](#insn-00affc98) 範囲 `[['00affc98', '00affca3']]`
  - `CONDITIONAL_JUMP` [`00affca0`](#insn-00affca0) → [`00affccc`](#insn-00affccc)
  - `FALL_THROUGH` [`00affca0`](#insn-00affca0) → [`00affca4`](#insn-00affca4)
- ブロック [`00affca4`](#insn-00affca4) 範囲 `[['00affca4', '00affcab']]`
  - `FALL_THROUGH` [`00affca8`](#insn-00affca8) → [`00affcac`](#insn-00affcac)
- ブロック [`00affcac`](#insn-00affcac) 範囲 `[['00affcac', '00affcaf']]`
  - `FALL_THROUGH` [`00affcac`](#insn-00affcac) → [`00affcb0`](#insn-00affcb0)
- ブロック [`00affcb0`](#insn-00affcb0) 範囲 `[['00affcb0', '00affcbb']]`
  - `FALL_THROUGH` [`00affcb8`](#insn-00affcb8) → [`00affcbc`](#insn-00affcbc)
- ブロック [`00affcbc`](#insn-00affcbc) 範囲 `[['00affcbc', '00affccb']]`
- ブロック [`00affccc`](#insn-00affccc) 範囲 `[['00affccc', '00affcd3']]`
  - `FALL_THROUGH` [`00affcd0`](#insn-00affcd0) → [`00affcd4`](#insn-00affcd4)
- ブロック [`00affcd4`](#insn-00affcd4) 範囲 `[['00affcd4', '00affcdb']]`
  - `CONDITIONAL_JUMP` [`00affcd8`](#insn-00affcd8) → [`00affcb0`](#insn-00affcb0)
  - `FALL_THROUGH` [`00affcd8`](#insn-00affcd8) → [`00affcdc`](#insn-00affcdc)
- ブロック [`00affcdc`](#insn-00affcdc) 範囲 `[['00affcdc', '00affcdf']]`
  - `FALL_THROUGH` [`00affcdc`](#insn-00affcdc) → [`00affce0`](#insn-00affce0)
- ブロック [`00affce0`](#insn-00affce0) 範囲 `[['00affce0', '00affce3']]`
  - `CONDITIONAL_JUMP` [`00affce0`](#insn-00affce0) → [`00affcac`](#insn-00affcac)
  - `FALL_THROUGH` [`00affce0`](#insn-00affce0) → [`00affce4`](#insn-00affce4)
- ブロック [`00affce4`](#insn-00affce4) 範囲 `[['00affce4', '00affceb']]`
  - `UNCONDITIONAL_JUMP` [`00affce8`](#insn-00affce8) → [`00affcb0`](#insn-00affcb0)

## 命令位置別の参照

- [`00affc3c`](#insn-00affc3c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc40`](#insn-00affc40) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc44`](#insn-00affc44) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc5c`](#insn-00affc5c) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00affc68`](#insn-00affc68) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00affc70`](#insn-00affc70) → [`00affca4`](#insn-00affca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc8c`](#insn-00affc8c) → [`00affc78`](#insn-00affc78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affc94`](#insn-00affc94) → [`00affca4`](#insn-00affca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affca0`](#insn-00affca0) → [`00affccc`](#insn-00affccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affca8`](#insn-00affca8) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affcb4`](#insn-00affcb4) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affcbc`](#insn-00affcbc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affcc0`](#insn-00affcc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affcd4`](#insn-00affcd4) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00affcd8`](#insn-00affcd8) → [`00affcb0`](#insn-00affcb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affce0`](#insn-00affce0) → [`00affcac`](#insn-00affcac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00affce8`](#insn-00affce8) → [`00affcb0`](#insn-00affcb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00affc3c`](#insn-00affc3c)

~~~json
{
  "source": "00affc3c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc40`](#insn-00affc40)

~~~json
{
  "source": "00affc40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc44`](#insn-00affc44)

~~~json
{
  "source": "00affc44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc5c`](#insn-00affc5c)

~~~json
{
  "source": "00affc5c",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affc68`](#insn-00affc68)

~~~json
{
  "source": "00affc68",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affc70`](#insn-00affc70)

~~~json
{
  "source": "00affc70",
  "target": "00affca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc8c`](#insn-00affc8c)

~~~json
{
  "source": "00affc8c",
  "target": "00affc78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affc94`](#insn-00affc94)

~~~json
{
  "source": "00affc94",
  "target": "00affca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affca0`](#insn-00affca0)

~~~json
{
  "source": "00affca0",
  "target": "00affccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affca8`](#insn-00affca8)

~~~json
{
  "source": "00affca8",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affcb4`](#insn-00affcb4)

~~~json
{
  "source": "00affcb4",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affcbc`](#insn-00affcbc)

~~~json
{
  "source": "00affcbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affcc0`](#insn-00affcc0)

~~~json
{
  "source": "00affcc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affcd4`](#insn-00affcd4)

~~~json
{
  "source": "00affcd4",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00affcd8`](#insn-00affcd8)

~~~json
{
  "source": "00affcd8",
  "target": "00affcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affce0`](#insn-00affce0)

~~~json
{
  "source": "00affce0",
  "target": "00affcac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00affce8`](#insn-00affce8)

~~~json
{
  "source": "00affce8",
  "target": "00affcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
