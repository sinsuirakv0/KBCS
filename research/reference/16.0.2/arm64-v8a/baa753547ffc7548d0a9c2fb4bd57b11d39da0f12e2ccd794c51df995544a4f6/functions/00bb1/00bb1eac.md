# 00bb1eac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb1e10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb1/00bb1e10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0010.md#compare-28d379302bc0723dd82f05d881987e5f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bb2ea0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2ea0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0035.md#compare-28efa0be6dc68d9a6652ab0cda67bfc9)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb1eac",
  "name": "FUN_00bb1eac",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d0d14b30347854c45f70a7c52cdd32f7a6ecbd598f596afd37e15b3fd05348c",
  "source_text_sha256": "5d0d14b30347854c45f70a7c52cdd32f7a6ecbd598f596afd37e15b3fd05348c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb1eac",
        "00bb1fb3"
      ]
    ],
    "bytes_sha256": "eaef0900550a5b73bf5e47f0ef733664ea0fa8a3a09a2f263c4aa807ae649e2c",
    "instruction_count": 66,
    "instruction_bytes": 264,
    "body_bytes": 264,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

- [00bb1810](../00bb1/00bb1810.md)
- [00bb2110](../00bb2/00bb2110.md)

## 呼び出し先

- [00c5d170](../00c5d/00c5d170.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1247 bytes

~~~c

int FUN_00bb1eac(undefined8 *param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4,
                undefined8 *param_5,undefined8 *param_6)

{
  int iVar1;
  ulong uVar2;
  undefined8 uVar3;
  
  iVar1 = _ZNSt6__ndk17__sort4IRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEjT0_SA_SA_SA_T_();
  uVar2 = (*(code *)*param_6)(*param_5,*param_4);
  if ((uVar2 & 1) != 0) {
    uVar3 = *param_4;
    *param_4 = *param_5;
    *param_5 = uVar3;
    uVar2 = (*(code *)*param_6)(*param_4,*param_3);
    if ((uVar2 & 1) == 0) {
      iVar1 = iVar1 + 1;
    }
    else {
                    /* catch() { ... } // from try @ 00bb2100 with catch @ 00bb1f24 */
      uVar3 = *param_3;
      *param_3 = *param_4;
      *param_4 = uVar3;
      uVar2 = (*(code *)*param_6)(*param_3,*param_2);
      if ((uVar2 & 1) == 0) {
        iVar1 = iVar1 + 2;
      }
      else {
        uVar3 = *param_2;
        *param_2 = *param_3;
        *param_3 = uVar3;
        uVar2 = (*(code *)*param_6)(*param_2,*param_1);
        if ((uVar2 & 1) == 0) {
          iVar1 = iVar1 + 3;
        }
        else {
          uVar3 = *param_1;
          iVar1 = iVar1 + 4;
          *param_1 = *param_2;
          *param_2 = uVar3;
        }
      }
    }
  }
  return iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb1eac"></a> `00bb1eac` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bb1eb0"></a> `00bb1eb0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb1eb4"></a> `00bb1eb4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb1eb8"></a> `00bb1eb8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb1ebc"></a> `00bb1ebc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb1ec0"></a> `00bb1ec0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bb1ec4"></a> `00bb1ec4` | `f9 03 04 aa` | mov x25,x4 | `FALL_THROUGH`
<a id="insn-00bb1ec8"></a> `00bb1ec8` | `e4 03 05 aa` | mov x4,x5 | `FALL_THROUGH`
<a id="insn-00bb1ecc"></a> `00bb1ecc` | `f6 03 05 aa` | mov x22,x5 | `FALL_THROUGH`
<a id="insn-00bb1ed0"></a> `00bb1ed0` | `f8 03 03 aa` | mov x24,x3 | `FALL_THROUGH`
<a id="insn-00bb1ed4"></a> `00bb1ed4` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bb1ed8"></a> `00bb1ed8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bb1edc"></a> `00bb1edc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bb1ee0"></a> `00bb1ee0` | `a4 ac 02 94` | bl 0x00c5d170 | `UNCONDITIONAL_CALL`
<a id="insn-00bb1ee4"></a> `00bb1ee4` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00bb1ee8"></a> `00bb1ee8` | `c9 02 40 f9` | ldr x9,[x22] | `FALL_THROUGH`
<a id="insn-00bb1eec"></a> `00bb1eec` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00bb1ef0"></a> `00bb1ef0` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bb1ef4"></a> `00bb1ef4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bb1ef8"></a> `00bb1ef8` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bb1efc"></a> `00bb1efc` | `e0 04 00 36` | tbz w0,#0x0,0x00bb1f98 | `CONDITIONAL_JUMP`
<a id="insn-00bb1f00"></a> `00bb1f00` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00bb1f04"></a> `00bb1f04` | `09 03 40 f9` | ldr x9,[x24] | `FALL_THROUGH`
<a id="insn-00bb1f08"></a> `00bb1f08` | `08 03 00 f9` | str x8,[x24] | `FALL_THROUGH`
<a id="insn-00bb1f0c"></a> `00bb1f0c` | `29 03 00 f9` | str x9,[x25] | `FALL_THROUGH`
<a id="insn-00bb1f10"></a> `00bb1f10` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bb1f14"></a> `00bb1f14` | `00 03 40 f9` | ldr x0,[x24] | `FALL_THROUGH`
<a id="insn-00bb1f18"></a> `00bb1f18` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00bb1f1c"></a> `00bb1f1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb1f20"></a> `00bb1f20` | `20 03 00 36` | tbz w0,#0x0,0x00bb1f84 | `CONDITIONAL_JUMP`
<a id="insn-00bb1f24"></a> `00bb1f24` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00bb1f28"></a> `00bb1f28` | `e9 02 40 f9` | ldr x9,[x23] | `FALL_THROUGH`
<a id="insn-00bb1f2c"></a> `00bb1f2c` | `e8 02 00 f9` | str x8,[x23] | `FALL_THROUGH`
<a id="insn-00bb1f30"></a> `00bb1f30` | `09 03 00 f9` | str x9,[x24] | `FALL_THROUGH`
<a id="insn-00bb1f34"></a> `00bb1f34` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bb1f38"></a> `00bb1f38` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00bb1f3c"></a> `00bb1f3c` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bb1f40"></a> `00bb1f40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb1f44"></a> `00bb1f44` | `40 02 00 36` | tbz w0,#0x0,0x00bb1f8c | `CONDITIONAL_JUMP`
<a id="insn-00bb1f48"></a> `00bb1f48` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bb1f4c"></a> `00bb1f4c` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bb1f50"></a> `00bb1f50` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00bb1f54"></a> `00bb1f54` | `e9 02 00 f9` | str x9,[x23] | `FALL_THROUGH`
<a id="insn-00bb1f58"></a> `00bb1f58` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bb1f5c"></a> `00bb1f5c` | `80 02 40 f9` | ldr x0,[x20] | `FALL_THROUGH`
<a id="insn-00bb1f60"></a> `00bb1f60` | `a1 02 40 f9` | ldr x1,[x21] | `FALL_THROUGH`
<a id="insn-00bb1f64"></a> `00bb1f64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bb1f68"></a> `00bb1f68` | `60 01 00 36` | tbz w0,#0x0,0x00bb1f94 | `CONDITIONAL_JUMP`
<a id="insn-00bb1f6c"></a> `00bb1f6c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bb1f70"></a> `00bb1f70` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00bb1f74"></a> `00bb1f74` | `73 12 00 11` | add w19,w19,#0x4 | `FALL_THROUGH`
<a id="insn-00bb1f78"></a> `00bb1f78` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00bb1f7c"></a> `00bb1f7c` | `89 02 00 f9` | str x9,[x20] | `FALL_THROUGH`
<a id="insn-00bb1f80"></a> `00bb1f80` | `06 00 00 14` | b 0x00bb1f98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb1f84"></a> `00bb1f84` | `73 06 00 11` | add w19,w19,#0x1 | `FALL_THROUGH`
<a id="insn-00bb1f88"></a> `00bb1f88` | `04 00 00 14` | b 0x00bb1f98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb1f8c"></a> `00bb1f8c` | `73 0a 00 11` | add w19,w19,#0x2 | `FALL_THROUGH`
<a id="insn-00bb1f90"></a> `00bb1f90` | `02 00 00 14` | b 0x00bb1f98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb1f94"></a> `00bb1f94` | `73 0e 00 11` | add w19,w19,#0x3 | `FALL_THROUGH`
<a id="insn-00bb1f98"></a> `00bb1f98` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bb1f9c"></a> `00bb1f9c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb1fa0"></a> `00bb1fa0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb1fa4"></a> `00bb1fa4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb1fa8"></a> `00bb1fa8` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb1fac"></a> `00bb1fac` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bb1fb0"></a> `00bb1fb0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb1eac`](#insn-00bb1eac) 範囲 `[['00bb1eac', '00bb1eff']]`
  - `CONDITIONAL_JUMP` [`00bb1efc`](#insn-00bb1efc) → [`00bb1f98`](#insn-00bb1f98)
  - `FALL_THROUGH` [`00bb1efc`](#insn-00bb1efc) → [`00bb1f00`](#insn-00bb1f00)
- ブロック [`00bb1f00`](#insn-00bb1f00) 範囲 `[['00bb1f00', '00bb1f23']]`
  - `CONDITIONAL_JUMP` [`00bb1f20`](#insn-00bb1f20) → [`00bb1f84`](#insn-00bb1f84)
  - `FALL_THROUGH` [`00bb1f20`](#insn-00bb1f20) → [`00bb1f24`](#insn-00bb1f24)
- ブロック [`00bb1f24`](#insn-00bb1f24) 範囲 `[['00bb1f24', '00bb1f47']]`
  - `CONDITIONAL_JUMP` [`00bb1f44`](#insn-00bb1f44) → [`00bb1f8c`](#insn-00bb1f8c)
  - `FALL_THROUGH` [`00bb1f44`](#insn-00bb1f44) → [`00bb1f48`](#insn-00bb1f48)
- ブロック [`00bb1f48`](#insn-00bb1f48) 範囲 `[['00bb1f48', '00bb1f6b']]`
  - `CONDITIONAL_JUMP` [`00bb1f68`](#insn-00bb1f68) → [`00bb1f94`](#insn-00bb1f94)
  - `FALL_THROUGH` [`00bb1f68`](#insn-00bb1f68) → [`00bb1f6c`](#insn-00bb1f6c)
- ブロック [`00bb1f6c`](#insn-00bb1f6c) 範囲 `[['00bb1f6c', '00bb1f83']]`
  - `UNCONDITIONAL_JUMP` [`00bb1f80`](#insn-00bb1f80) → [`00bb1f98`](#insn-00bb1f98)
- ブロック [`00bb1f84`](#insn-00bb1f84) 範囲 `[['00bb1f84', '00bb1f8b']]`
  - `UNCONDITIONAL_JUMP` [`00bb1f88`](#insn-00bb1f88) → [`00bb1f98`](#insn-00bb1f98)
- ブロック [`00bb1f8c`](#insn-00bb1f8c) 範囲 `[['00bb1f8c', '00bb1f93']]`
  - `UNCONDITIONAL_JUMP` [`00bb1f90`](#insn-00bb1f90) → [`00bb1f98`](#insn-00bb1f98)
- ブロック [`00bb1f94`](#insn-00bb1f94) 範囲 `[['00bb1f94', '00bb1f97']]`
  - `FALL_THROUGH` [`00bb1f94`](#insn-00bb1f94) → [`00bb1f98`](#insn-00bb1f98)
- ブロック [`00bb1f98`](#insn-00bb1f98) 範囲 `[['00bb1f98', '00bb1fb3']]`

## 命令位置別の参照

- [`00bb1eac`](#insn-00bb1eac) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1eb0`](#insn-00bb1eb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1eb4`](#insn-00bb1eb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1eb8`](#insn-00bb1eb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1ebc`](#insn-00bb1ebc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1ee0`](#insn-00bb1ee0) → [`00c5d170`](../00c5d/00c5d170.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d170` · 推定シンボル `None` · 推定型 `None`
- [`00bb1efc`](#insn-00bb1efc) → [`00bb1f98`](#insn-00bb1f98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f20`](#insn-00bb1f20) → [`00bb1f84`](#insn-00bb1f84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f44`](#insn-00bb1f44) → [`00bb1f8c`](#insn-00bb1f8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f68`](#insn-00bb1f68) → [`00bb1f94`](#insn-00bb1f94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f80`](#insn-00bb1f80) → [`00bb1f98`](#insn-00bb1f98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f88`](#insn-00bb1f88) → [`00bb1f98`](#insn-00bb1f98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f90`](#insn-00bb1f90) → [`00bb1f98`](#insn-00bb1f98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f9c`](#insn-00bb1f9c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1fa0`](#insn-00bb1fa0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1fa4`](#insn-00bb1fa4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1fa8`](#insn-00bb1fa8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb1eac`](#insn-00bb1eac)

~~~json
{
  "source": "00bb1eac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1eb0`](#insn-00bb1eb0)

~~~json
{
  "source": "00bb1eb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1eb4`](#insn-00bb1eb4)

~~~json
{
  "source": "00bb1eb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1eb8`](#insn-00bb1eb8)

~~~json
{
  "source": "00bb1eb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1ebc`](#insn-00bb1ebc)

~~~json
{
  "source": "00bb1ebc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1ee0`](#insn-00bb1ee0)

~~~json
{
  "source": "00bb1ee0",
  "target": "00c5d170",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb1efc`](#insn-00bb1efc)

~~~json
{
  "source": "00bb1efc",
  "target": "00bb1f98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f20`](#insn-00bb1f20)

~~~json
{
  "source": "00bb1f20",
  "target": "00bb1f84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f44`](#insn-00bb1f44)

~~~json
{
  "source": "00bb1f44",
  "target": "00bb1f8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f68`](#insn-00bb1f68)

~~~json
{
  "source": "00bb1f68",
  "target": "00bb1f94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f80`](#insn-00bb1f80)

~~~json
{
  "source": "00bb1f80",
  "target": "00bb1f98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f88`](#insn-00bb1f88)

~~~json
{
  "source": "00bb1f88",
  "target": "00bb1f98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f90`](#insn-00bb1f90)

~~~json
{
  "source": "00bb1f90",
  "target": "00bb1f98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f9c`](#insn-00bb1f9c)

~~~json
{
  "source": "00bb1f9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1fa0`](#insn-00bb1fa0)

~~~json
{
  "source": "00bb1fa0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1fa4`](#insn-00bb1fa4)

~~~json
{
  "source": "00bb1fa4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1fa8`](#insn-00bb1fa8)

~~~json
{
  "source": "00bb1fa8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
