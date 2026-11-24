# 00bde2cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bddea4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bddea4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0010.md#compare-c4ac328da3b4b78e9694c0458b16d33a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bde368`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde368.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0010.md#compare-cbb0b30fa956d0a538bbe8d8dffc6e7f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bde2cc",
  "name": "_ZNK8firebase4auth4User3uidEv",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1c3d840a10f662bbc468e7bfa1cd5b8f09804c45652678e15a59277de3073040",
  "source_text_sha256": "1c3d840a10f662bbc468e7bfa1cd5b8f09804c45652678e15a59277de3073040",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bde2cc",
        "00bde36f"
      ]
    ],
    "bytes_sha256": "5715715dcdee4d4819af9c4332c855fed38300f4aafde98360703791c7c74f35",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497834](../00497/00497834.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b390](../00c5b/00c5b390.md)
- [00c5b5c0](../00c5b/00c5b5c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 787 bytes

~~~c

void _ZNK8firebase4auth4User3uidEv(undefined8 *param_1,long param_2)

{
  undefined8 uVar1;
  ulong uVar2;
  undefined8 *puVar3;
  long lVar4;
  
  puVar3 = *(undefined8 **)(param_2 + 0x98);
  if ((puVar3 == (undefined8 *)0x0) || (lVar4 = puVar3[0x40], lVar4 == 0)) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
              (param_1,&DAT_002a63ea);
    return;
  }
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*puVar3);
  lVar4 = FUN_00497834(uVar1,lVar4,DAT_01126dc0);
  uVar2 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
  if ((lVar4 != 0) && ((uVar2 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar1,lVar4);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bde2cc"></a> `00bde2cc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bde2d0"></a> `00bde2d0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde2d4"></a> `00bde2d4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bde2d8"></a> `00bde2d8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bde2dc"></a> `00bde2dc` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bde2e0"></a> `00bde2e0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bde2e4"></a> `00bde2e4` | `c9 02 00 b4` | cbz x9,0x00bde33c | `CONDITIONAL_JUMP`
<a id="insn-00bde2e8"></a> `00bde2e8` | `35 01 41 f9` | ldr x21,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00bde2ec"></a> `00bde2ec` | `95 02 00 b4` | cbz x21,0x00bde33c | `CONDITIONAL_JUMP`
<a id="insn-00bde2f0"></a> `00bde2f0` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bde2f4"></a> `00bde2f4` | `63 f3 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bde2f8"></a> `00bde2f8` | `48 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bde2fc"></a> `00bde2fc` | `02 e1 46 f9` | ldr x2,[x8, #0xdc0] | `FALL_THROUGH`
<a id="insn-00bde300"></a> `00bde300` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bde304"></a> `00bde304` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bde308"></a> `00bde308` | `4b e5 e2 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bde30c"></a> `00bde30c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bde310"></a> `00bde310` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bde314"></a> `00bde314` | `13 f3 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bde318"></a> `00bde318` | `15 02 00 b4` | cbz x21,0x00bde358 | `CONDITIONAL_JUMP`
<a id="insn-00bde31c"></a> `00bde31c` | `e0 01 00 37` | tbnz w0,#0x0,0x00bde358 | `CONDITIONAL_JUMP`
<a id="insn-00bde320"></a> `00bde320` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bde324"></a> `00bde324` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bde328"></a> `00bde328` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bde32c"></a> `00bde32c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde330"></a> `00bde330` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bde334"></a> `00bde334` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bde338"></a> `00bde338` | `16 f4 01 14` | b 0x00c5b390 | `CALL_TERMINATOR`
<a id="insn-00bde33c"></a> `00bde33c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bde340"></a> `00bde340` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bde344"></a> `00bde344` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde348"></a> `00bde348` | `41 b6 ff 90` | adrp x1,0x2a6000 | `FALL_THROUGH`
<a id="insn-00bde34c"></a> `00bde34c` | `21 a8 0f 91` | add x1,x1,#0x3ea | `FALL_THROUGH`
<a id="insn-00bde350"></a> `00bde350` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bde354"></a> `00bde354` | `9b f4 01 14` | b 0x00c5b5c0 | `CALL_TERMINATOR`
<a id="insn-00bde358"></a> `00bde358` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bde35c"></a> `00bde35c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bde360"></a> `00bde360` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bde364"></a> `00bde364` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde368"></a> `00bde368` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bde36c"></a> `00bde36c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bde2cc`](#insn-00bde2cc) 範囲 `[['00bde2cc', '00bde2e7']]`
  - `CONDITIONAL_JUMP` [`00bde2e4`](#insn-00bde2e4) → [`00bde33c`](#insn-00bde33c)
  - `FALL_THROUGH` [`00bde2e4`](#insn-00bde2e4) → [`00bde2e8`](#insn-00bde2e8)
- ブロック [`00bde2e8`](#insn-00bde2e8) 範囲 `[['00bde2e8', '00bde2ef']]`
  - `CONDITIONAL_JUMP` [`00bde2ec`](#insn-00bde2ec) → [`00bde33c`](#insn-00bde33c)
  - `FALL_THROUGH` [`00bde2ec`](#insn-00bde2ec) → [`00bde2f0`](#insn-00bde2f0)
- ブロック [`00bde2f0`](#insn-00bde2f0) 範囲 `[['00bde2f0', '00bde31b']]`
  - `CONDITIONAL_JUMP` [`00bde318`](#insn-00bde318) → [`00bde358`](#insn-00bde358)
  - `FALL_THROUGH` [`00bde318`](#insn-00bde318) → [`00bde31c`](#insn-00bde31c)
- ブロック [`00bde31c`](#insn-00bde31c) 範囲 `[['00bde31c', '00bde31f']]`
  - `CONDITIONAL_JUMP` [`00bde31c`](#insn-00bde31c) → [`00bde358`](#insn-00bde358)
  - `FALL_THROUGH` [`00bde31c`](#insn-00bde31c) → [`00bde320`](#insn-00bde320)
- ブロック [`00bde320`](#insn-00bde320) 範囲 `[['00bde320', '00bde33b']]`
- ブロック [`00bde33c`](#insn-00bde33c) 範囲 `[['00bde33c', '00bde357']]`
- ブロック [`00bde358`](#insn-00bde358) 範囲 `[['00bde358', '00bde36f']]`

## 命令位置別の参照

- [`00bde2cc`](#insn-00bde2cc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde2d0`](#insn-00bde2d0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde2d4`](#insn-00bde2d4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde2e4`](#insn-00bde2e4) → [`00bde33c`](#insn-00bde33c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde2ec`](#insn-00bde2ec) → [`00bde33c`](#insn-00bde33c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde2f4`](#insn-00bde2f4) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bde2fc`](#insn-00bde2fc) → `01126dc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bde308`](#insn-00bde308) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bde314`](#insn-00bde314) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bde318`](#insn-00bde318) → [`00bde358`](#insn-00bde358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde31c`](#insn-00bde31c) → [`00bde358`](#insn-00bde358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde328`](#insn-00bde328) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde32c`](#insn-00bde32c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde338`](#insn-00bde338) → [`00c5b390`](../00c5b/00c5b390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b390` · 推定シンボル `None` · 推定型 `None`
- [`00bde340`](#insn-00bde340) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde344`](#insn-00bde344) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde34c`](#insn-00bde34c) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bde354`](#insn-00bde354) → [`00c5b5c0`](../00c5b/00c5b5c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b5c0` · 推定シンボル `None` · 推定型 `None`
- [`00bde360`](#insn-00bde360) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde364`](#insn-00bde364) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bde2cc`](#insn-00bde2cc)

~~~json
{
  "source": "00bde2cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde2d0`](#insn-00bde2d0)

~~~json
{
  "source": "00bde2d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde2d4`](#insn-00bde2d4)

~~~json
{
  "source": "00bde2d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde2e4`](#insn-00bde2e4)

~~~json
{
  "source": "00bde2e4",
  "target": "00bde33c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde2ec`](#insn-00bde2ec)

~~~json
{
  "source": "00bde2ec",
  "target": "00bde33c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde2f4`](#insn-00bde2f4)

~~~json
{
  "source": "00bde2f4",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde2fc`](#insn-00bde2fc)

~~~json
{
  "source": "00bde2fc",
  "target": "01126dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126dc0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde308`](#insn-00bde308)

~~~json
{
  "source": "00bde308",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde314`](#insn-00bde314)

~~~json
{
  "source": "00bde314",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde318`](#insn-00bde318)

~~~json
{
  "source": "00bde318",
  "target": "00bde358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde31c`](#insn-00bde31c)

~~~json
{
  "source": "00bde31c",
  "target": "00bde358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde328`](#insn-00bde328)

~~~json
{
  "source": "00bde328",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde32c`](#insn-00bde32c)

~~~json
{
  "source": "00bde32c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde338`](#insn-00bde338)

~~~json
{
  "source": "00bde338",
  "target": "00c5b390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde340`](#insn-00bde340)

~~~json
{
  "source": "00bde340",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde344`](#insn-00bde344)

~~~json
{
  "source": "00bde344",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde34c`](#insn-00bde34c)

~~~json
{
  "source": "00bde34c",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bde354`](#insn-00bde354)

~~~json
{
  "source": "00bde354",
  "target": "00c5b5c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde360`](#insn-00bde360)

~~~json
{
  "source": "00bde360",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde364`](#insn-00bde364)

~~~json
{
  "source": "00bde364",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
