# 00aeacc8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aead90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aead90.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-d88bd20dc0fc0c626c7cb1331f4068d9)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeacc8",
  "name": "_ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "60e2b96c628a32ebba219e22bebb7e500956adb53cb510f8d11f3ed101975393",
  "source_text_sha256": "60e2b96c628a32ebba219e22bebb7e500956adb53cb510f8d11f3ed101975393",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeacc8",
        "00aead63"
      ]
    ],
    "bytes_sha256": "4d4744cb8ffe3667919d92008df0d8f8c166ac715608319920e7ffb2d4c3dea6",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 693 bytes

~~~c

bool _ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a0758 == '\0') {
                    /* catch() { ... } // from try @ 00aeab8c with catch @ 00aeacf8 */
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a0750,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a0758 = iVar3 == 0;
    bVar2 = (bool)DAT_010a0758;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeacc8"></a> `00aeacc8` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aeaccc"></a> `00aeaccc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeacd0"></a> `00aeacd0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aeacd4"></a> `00aeacd4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aeacd8"></a> `00aeacd8` | `b5 2d 00 d0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeacdc"></a> `00aeacdc` | `a8 62 5d 39` | ldrb w8,[x21, #0x758] | `FALL_THROUGH`
<a id="insn-00aeace0"></a> `00aeace0` | `68 00 00 34` | cbz w8,0x00aeacec | `CONDITIONAL_JUMP`
<a id="insn-00aeace4"></a> `00aeace4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aeace8"></a> `00aeace8` | `1b 00 00 14` | b 0x00aead54 | `UNCONDITIONAL_JUMP`
<a id="insn-00aeacec"></a> `00aeacec` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aeacf0"></a> `00aeacf0` | `a9 2d 00 d0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeacf4"></a> `00aeacf4` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00aeacf8"></a> `00aeacf8` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00aeacfc"></a> `00aeacfc` | `21 a9 43 f9` | ldr x1,[x9, #0x750] | `FALL_THROUGH`
<a id="insn-00aead00"></a> `00aead00` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00aead04"></a> `00aead04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aead08"></a> `00aead08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aead0c"></a> `00aead0c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aead10"></a> `00aead10` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aead14"></a> `00aead14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aead18"></a> `00aead18` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aead1c"></a> `00aead1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aead20"></a> `00aead20` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aead24"></a> `00aead24` | `20 01 00 54` | b.eq 0x00aead48 | `CONDITIONAL_JUMP`
<a id="insn-00aead28"></a> `00aead28` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aead2c"></a> `00aead2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aead30"></a> `00aead30` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aead34"></a> `00aead34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aead38"></a> `00aead38` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aead3c"></a> `00aead3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aead40"></a> `00aead40` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aead44"></a> `00aead44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aead48"></a> `00aead48` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00aead4c"></a> `00aead4c` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00aead50"></a> `00aead50` | `a0 62 1d 39` | strb w0,[x21, #0x758] | `FALL_THROUGH`
<a id="insn-00aead54"></a> `00aead54` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aead58"></a> `00aead58` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aead5c"></a> `00aead5c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aead60"></a> `00aead60` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeacc8`](#insn-00aeacc8) 範囲 `[['00aeacc8', '00aeace3']]`
  - `CONDITIONAL_JUMP` [`00aeace0`](#insn-00aeace0) → [`00aeacec`](#insn-00aeacec)
  - `FALL_THROUGH` [`00aeace0`](#insn-00aeace0) → [`00aeace4`](#insn-00aeace4)
- ブロック [`00aeace4`](#insn-00aeace4) 範囲 `[['00aeace4', '00aeaceb']]`
  - `UNCONDITIONAL_JUMP` [`00aeace8`](#insn-00aeace8) → [`00aead54`](#insn-00aead54)
- ブロック [`00aeacec`](#insn-00aeacec) 範囲 `[['00aeacec', '00aeacf7']]`
  - `FALL_THROUGH` [`00aeacf4`](#insn-00aeacf4) → [`00aeacf8`](#insn-00aeacf8)
- ブロック [`00aeacf8`](#insn-00aeacf8) 範囲 `[['00aeacf8', '00aead27']]`
  - `CONDITIONAL_JUMP` [`00aead24`](#insn-00aead24) → [`00aead48`](#insn-00aead48)
  - `FALL_THROUGH` [`00aead24`](#insn-00aead24) → [`00aead28`](#insn-00aead28)
- ブロック [`00aead28`](#insn-00aead28) 範囲 `[['00aead28', '00aead47']]`
  - `FALL_THROUGH` [`00aead44`](#insn-00aead44) → [`00aead48`](#insn-00aead48)
- ブロック [`00aead48`](#insn-00aead48) 範囲 `[['00aead48', '00aead53']]`
  - `FALL_THROUGH` [`00aead50`](#insn-00aead50) → [`00aead54`](#insn-00aead54)
- ブロック [`00aead54`](#insn-00aead54) 範囲 `[['00aead54', '00aead63']]`

## 命令位置別の参照

- [`00aeacc8`](#insn-00aeacc8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaccc`](#insn-00aeaccc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeacd0`](#insn-00aeacd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeacdc`](#insn-00aeacdc) → `010a0758`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aeace0`](#insn-00aeace0) → [`00aeacec`](#insn-00aeacec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeace8`](#insn-00aeace8) → [`00aead54`](#insn-00aead54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeacfc`](#insn-00aeacfc) → `010a0750`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aead24`](#insn-00aead24) → [`00aead48`](#insn-00aead48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aead50`](#insn-00aead50) → `010a0758`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aead54`](#insn-00aead54) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aead58`](#insn-00aead58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeacc8`](#insn-00aeacc8)

~~~json
{
  "source": "00aeacc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaccc`](#insn-00aeaccc)

~~~json
{
  "source": "00aeaccc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeacd0`](#insn-00aeacd0)

~~~json
{
  "source": "00aeacd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeacdc`](#insn-00aeacdc)

~~~json
{
  "source": "00aeacdc",
  "target": "010a0758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0758",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeace0`](#insn-00aeace0)

~~~json
{
  "source": "00aeace0",
  "target": "00aeacec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeace8`](#insn-00aeace8)

~~~json
{
  "source": "00aeace8",
  "target": "00aead54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeacfc`](#insn-00aeacfc)

~~~json
{
  "source": "00aeacfc",
  "target": "010a0750",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0750",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aead24`](#insn-00aead24)

~~~json
{
  "source": "00aead24",
  "target": "00aead48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aead50`](#insn-00aead50)

~~~json
{
  "source": "00aead50",
  "target": "010a0758",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0758",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aead54`](#insn-00aead54)

~~~json
{
  "source": "00aead54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aead58`](#insn-00aead58)

~~~json
{
  "source": "00aead58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
