# 00b6ebcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b6ec94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ec94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0073.md#compare-c492790b916368013936f55a40120f3a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6ebcc",
  "name": "_ZNK8firebase4auth4User11provider_idEv",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0c0e1e46b81714489e898a346c0ec408146364f5ea4108f20b008e23c84005d2",
  "source_text_sha256": "0c0e1e46b81714489e898a346c0ec408146364f5ea4108f20b008e23c84005d2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6ebcc",
        "00b6ec6f"
      ]
    ],
    "bytes_sha256": "59b297adbf92ea5a1b9f91506a88c112388b72fcbc861771d122a6787e1cb214",
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

- [0047495c](../00474/0047495c.md)
- [00bddfe0](../00bdd/00bddfe0.md)
- [00bde100](../00bde/00bde100.md)
- [00bde410](../00bde/00bde410.md)
- [00bde640](../00bde/00bde640.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 990 bytes

~~~c

void _ZNK8firebase4auth4User11provider_idEv(undefined8 *param_1,long param_2)

{
  undefined8 uVar1;
  ulong uVar2;
  undefined8 *puVar3;
  long lVar4;
  
  puVar3 = *(undefined8 **)(param_2 + 0x98);
  if ((puVar3 == (undefined8 *)0x0) || (lVar4 = puVar3[0x40], lVar4 == 0)) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
              (param_1,&DAT_002967d9);
    return;
  }
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*puVar3);
                    /* try { // try from 00b6ebf8 to 00c6ec0f has its CatchHandler @ 00b70724 */
  lVar4 = FUN_0047495c(uVar1,lVar4,DAT_010a19c0);
                    /* try { // try from 00b6ec10 to 00c6ecbb has its CatchHandler @ 00b6e3fc */
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
<a id="insn-00b6ebcc"></a> `00b6ebcc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b6ebd0"></a> `00b6ebd0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ebd4"></a> `00b6ebd4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6ebd8"></a> `00b6ebd8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b6ebdc"></a> `00b6ebdc` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00b6ebe0"></a> `00b6ebe0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b6ebe4"></a> `00b6ebe4` | `c9 02 00 b4` | cbz x9,0x00b6ec3c | `CONDITIONAL_JUMP`
<a id="insn-00b6ebe8"></a> `00b6ebe8` | `35 01 41 f9` | ldr x21,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00b6ebec"></a> `00b6ebec` | `95 02 00 b4` | cbz x21,0x00b6ec3c | `CONDITIONAL_JUMP`
<a id="insn-00b6ebf0"></a> `00b6ebf0` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00b6ebf4"></a> `00b6ebf4` | `43 bd 01 94` | bl 0x00bde100 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ebf8"></a> `00b6ebf8` | `88 29 00 f0` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6ebfc"></a> `00b6ebfc` | `02 e1 44 f9` | ldr x2,[x8, #0x9c0] | `FALL_THROUGH`
<a id="insn-00b6ec00"></a> `00b6ec00` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b6ec04"></a> `00b6ec04` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b6ec08"></a> `00b6ec08` | `55 17 e4 97` | bl 0x0047495c | `UNCONDITIONAL_CALL`
<a id="insn-00b6ec0c"></a> `00b6ec0c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b6ec10"></a> `00b6ec10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6ec14"></a> `00b6ec14` | `f3 bc 01 94` | bl 0x00bddfe0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ec18"></a> `00b6ec18` | `15 02 00 b4` | cbz x21,0x00b6ec58 | `CONDITIONAL_JUMP`
<a id="insn-00b6ec1c"></a> `00b6ec1c` | `e0 01 00 37` | tbnz w0,#0x0,0x00b6ec58 | `CONDITIONAL_JUMP`
<a id="insn-00b6ec20"></a> `00b6ec20` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b6ec24"></a> `00b6ec24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6ec28"></a> `00b6ec28` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6ec2c"></a> `00b6ec2c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ec30"></a> `00b6ec30` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b6ec34"></a> `00b6ec34` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6ec38"></a> `00b6ec38` | `f6 bd 01 14` | b 0x00bde410 | `CALL_TERMINATOR`
<a id="insn-00b6ec3c"></a> `00b6ec3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6ec40"></a> `00b6ec40` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6ec44"></a> `00b6ec44` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ec48"></a> `00b6ec48` | `41 b9 ff 90` | adrp x1,0x296000 | `FALL_THROUGH`
<a id="insn-00b6ec4c"></a> `00b6ec4c` | `21 64 1f 91` | add x1,x1,#0x7d9 | `FALL_THROUGH`
<a id="insn-00b6ec50"></a> `00b6ec50` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6ec54"></a> `00b6ec54` | `7b be 01 14` | b 0x00bde640 | `CALL_TERMINATOR`
<a id="insn-00b6ec58"></a> `00b6ec58` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b6ec5c"></a> `00b6ec5c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ec60"></a> `00b6ec60` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6ec64"></a> `00b6ec64` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ec68"></a> `00b6ec68` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6ec6c"></a> `00b6ec6c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6ebcc`](#insn-00b6ebcc) 範囲 `[['00b6ebcc', '00b6ebe7']]`
  - `CONDITIONAL_JUMP` [`00b6ebe4`](#insn-00b6ebe4) → [`00b6ec3c`](#insn-00b6ec3c)
  - `FALL_THROUGH` [`00b6ebe4`](#insn-00b6ebe4) → [`00b6ebe8`](#insn-00b6ebe8)
- ブロック [`00b6ebe8`](#insn-00b6ebe8) 範囲 `[['00b6ebe8', '00b6ebef']]`
  - `CONDITIONAL_JUMP` [`00b6ebec`](#insn-00b6ebec) → [`00b6ec3c`](#insn-00b6ec3c)
  - `FALL_THROUGH` [`00b6ebec`](#insn-00b6ebec) → [`00b6ebf0`](#insn-00b6ebf0)
- ブロック [`00b6ebf0`](#insn-00b6ebf0) 範囲 `[['00b6ebf0', '00b6ebf7']]`
  - `FALL_THROUGH` [`00b6ebf4`](#insn-00b6ebf4) → [`00b6ebf8`](#insn-00b6ebf8)
- ブロック [`00b6ebf8`](#insn-00b6ebf8) 範囲 `[['00b6ebf8', '00b6ec0f']]`
  - `FALL_THROUGH` [`00b6ec0c`](#insn-00b6ec0c) → [`00b6ec10`](#insn-00b6ec10)
- ブロック [`00b6ec10`](#insn-00b6ec10) 範囲 `[['00b6ec10', '00b6ec1b']]`
  - `CONDITIONAL_JUMP` [`00b6ec18`](#insn-00b6ec18) → [`00b6ec58`](#insn-00b6ec58)
  - `FALL_THROUGH` [`00b6ec18`](#insn-00b6ec18) → [`00b6ec1c`](#insn-00b6ec1c)
- ブロック [`00b6ec1c`](#insn-00b6ec1c) 範囲 `[['00b6ec1c', '00b6ec1f']]`
  - `CONDITIONAL_JUMP` [`00b6ec1c`](#insn-00b6ec1c) → [`00b6ec58`](#insn-00b6ec58)
  - `FALL_THROUGH` [`00b6ec1c`](#insn-00b6ec1c) → [`00b6ec20`](#insn-00b6ec20)
- ブロック [`00b6ec20`](#insn-00b6ec20) 範囲 `[['00b6ec20', '00b6ec3b']]`
- ブロック [`00b6ec3c`](#insn-00b6ec3c) 範囲 `[['00b6ec3c', '00b6ec57']]`
- ブロック [`00b6ec58`](#insn-00b6ec58) 範囲 `[['00b6ec58', '00b6ec6f']]`

## 命令位置別の参照

- [`00b6ebcc`](#insn-00b6ebcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ebd0`](#insn-00b6ebd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ebd4`](#insn-00b6ebd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ebe4`](#insn-00b6ebe4) → [`00b6ec3c`](#insn-00b6ec3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ebec`](#insn-00b6ebec) → [`00b6ec3c`](#insn-00b6ec3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ebf4`](#insn-00b6ebf4) → [`00bde100`](../00bde/00bde100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde100` · 推定シンボル `None` · 推定型 `None`
- [`00b6ebfc`](#insn-00b6ebfc) → `010a19c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6ec08`](#insn-00b6ec08) → [`0047495c`](../00474/0047495c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047495c` · 推定シンボル `None` · 推定型 `None`
- [`00b6ec14`](#insn-00b6ec14) → [`00bddfe0`](../00bdd/00bddfe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfe0` · 推定シンボル `None` · 推定型 `None`
- [`00b6ec18`](#insn-00b6ec18) → [`00b6ec58`](#insn-00b6ec58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ec1c`](#insn-00b6ec1c) → [`00b6ec58`](#insn-00b6ec58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ec28`](#insn-00b6ec28) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ec2c`](#insn-00b6ec2c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ec38`](#insn-00b6ec38) → [`00bde410`](../00bde/00bde410.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde410` · 推定シンボル `None` · 推定型 `None`
- [`00b6ec40`](#insn-00b6ec40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ec44`](#insn-00b6ec44) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ec4c`](#insn-00b6ec4c) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b6ec54`](#insn-00b6ec54) → [`00bde640`](../00bde/00bde640.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde640` · 推定シンボル `None` · 推定型 `None`
- [`00b6ec60`](#insn-00b6ec60) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ec64`](#insn-00b6ec64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6ebcc`](#insn-00b6ebcc)

~~~json
{
  "source": "00b6ebcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ebd0`](#insn-00b6ebd0)

~~~json
{
  "source": "00b6ebd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ebd4`](#insn-00b6ebd4)

~~~json
{
  "source": "00b6ebd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ebe4`](#insn-00b6ebe4)

~~~json
{
  "source": "00b6ebe4",
  "target": "00b6ec3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ebec`](#insn-00b6ebec)

~~~json
{
  "source": "00b6ebec",
  "target": "00b6ec3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ebf4`](#insn-00b6ebf4)

~~~json
{
  "source": "00b6ebf4",
  "target": "00bde100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ebfc`](#insn-00b6ebfc)

~~~json
{
  "source": "00b6ebfc",
  "target": "010a19c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a19c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6ec08`](#insn-00b6ec08)

~~~json
{
  "source": "00b6ec08",
  "target": "0047495c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ec14`](#insn-00b6ec14)

~~~json
{
  "source": "00b6ec14",
  "target": "00bddfe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ec18`](#insn-00b6ec18)

~~~json
{
  "source": "00b6ec18",
  "target": "00b6ec58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ec1c`](#insn-00b6ec1c)

~~~json
{
  "source": "00b6ec1c",
  "target": "00b6ec58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ec28`](#insn-00b6ec28)

~~~json
{
  "source": "00b6ec28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ec2c`](#insn-00b6ec2c)

~~~json
{
  "source": "00b6ec2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ec38`](#insn-00b6ec38)

~~~json
{
  "source": "00b6ec38",
  "target": "00bde410",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ec40`](#insn-00b6ec40)

~~~json
{
  "source": "00b6ec40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ec44`](#insn-00b6ec44)

~~~json
{
  "source": "00b6ec44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ec4c`](#insn-00b6ec4c)

~~~json
{
  "source": "00b6ec4c",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b6ec54`](#insn-00b6ec54)

~~~json
{
  "source": "00b6ec54",
  "target": "00bde640",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ec60`](#insn-00b6ec60)

~~~json
{
  "source": "00b6ec60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ec64`](#insn-00b6ec64)

~~~json
{
  "source": "00b6ec64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
