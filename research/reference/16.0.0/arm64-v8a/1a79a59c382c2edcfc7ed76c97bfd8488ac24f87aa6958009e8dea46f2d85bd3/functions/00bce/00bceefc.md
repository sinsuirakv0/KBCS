# 00bceefc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5f9fc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f9fc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0067.md#compare-a4686213eb7a61ab76b00497d6cae27c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcf324`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf324.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-5ac0b05a9b25ea0d1101fdc1c1dd0d27)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bceefc",
  "name": "_ZN8firebase4auth4Auth17set_language_codeEPKc",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cebe7eb3785ec2225abda950424c3a756037a2bc3d7d652dfbb633934c693884",
  "source_text_sha256": "cebe7eb3785ec2225abda950424c3a756037a2bc3d7d652dfbb633934c693884",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bceefc",
        "00bcef9b"
      ]
    ],
    "bytes_sha256": "d8dafd124165a2421bf306cdc4ee8e0e3cf5463d69b0aa622b18a749772d631f",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00574cac](../00574/00574cac.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac80](../00c5a/00c5ac80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1051 bytes

~~~c

void _ZN8firebase4auth4Auth17set_language_codeEPKc(long *param_1,long param_2)

{
  long *plVar1;
  long lVar2;
  
  if ((undefined8 *)*param_1 != (undefined8 *)0x0) {
    plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_1);
    lVar2 = 0;
    if (param_2 != 0) {
      lVar2 = (**(code **)(*plVar1 + 0x538))(plVar1,param_2);
    }
    FUN_00574cac(plVar1,*(undefined8 *)(*param_1 + 0x1f8),DAT_01126350,lVar2);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar1);
    if (lVar2 != 0) {
                    /* try { // try from 00bcef7c to 00ccef83 has its CatchHandler @ 00bcef84 */
                    /* catch() { ... } // from try @ 00bcef7c with catch @ 00bcef84
                       try { // try from 00bcef84 to 00ccefbb has its CatchHandler @ 00bcec24 */
                    /* WARNING: Could not recover jumptable at 0x00bcef88. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*plVar1 + 0xb8))(plVar1,lVar2);
      return;
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bceefc"></a> `00bceefc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcef00"></a> `00bcef00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcef04"></a> `00bcef04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcef08"></a> `00bcef08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcef0c"></a> `00bcef0c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcef10"></a> `00bcef10` | `e8 03 00 b4` | cbz x8,0x00bcef8c | `CONDITIONAL_JUMP`
<a id="insn-00bcef14"></a> `00bcef14` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcef18"></a> `00bcef18` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcef1c"></a> `00bcef1c` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bcef20"></a> `00bcef20` | `58 2f 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcef24"></a> `00bcef24` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcef28"></a> `00bcef28` | `f5 00 00 b4` | cbz x21,0x00bcef44 | `CONDITIONAL_JUMP`
<a id="insn-00bcef2c"></a> `00bcef2c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcef30"></a> `00bcef30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcef34"></a> `00bcef34` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcef38"></a> `00bcef38` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bcef3c"></a> `00bcef3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcef40"></a> `00bcef40` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcef44"></a> `00bcef44` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcef48"></a> `00bcef48` | `c9 2a 00 90` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcef4c"></a> `00bcef4c` | `22 a9 41 f9` | ldr x2,[x9, #0x350] | `FALL_THROUGH`
<a id="insn-00bcef50"></a> `00bcef50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcef54"></a> `00bcef54` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bcef58"></a> `00bcef58` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00bcef5c"></a> `00bcef5c` | `54 97 e6 97` | bl 0x00574cac | `UNCONDITIONAL_CALL`
<a id="insn-00bcef60"></a> `00bcef60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcef64"></a> `00bcef64` | `ff 2e 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcef68"></a> `00bcef68` | `35 01 00 b4` | cbz x21,0x00bcef8c | `CONDITIONAL_JUMP`
<a id="insn-00bcef6c"></a> `00bcef6c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcef70"></a> `00bcef70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcef74"></a> `00bcef74` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcef78"></a> `00bcef78` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcef7c"></a> `00bcef7c` | `02 5d 40 f9` | ldr x2,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcef80"></a> `00bcef80` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcef84"></a> `00bcef84` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcef88"></a> `00bcef88` | `40 00 1f d6` | br x2 | `COMPUTED_JUMP`
<a id="insn-00bcef8c"></a> `00bcef8c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcef90"></a> `00bcef90` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcef94"></a> `00bcef94` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcef98"></a> `00bcef98` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bceefc`](#insn-00bceefc) 範囲 `[['00bceefc', '00bcef13']]`
  - `CONDITIONAL_JUMP` [`00bcef10`](#insn-00bcef10) → [`00bcef8c`](#insn-00bcef8c)
  - `FALL_THROUGH` [`00bcef10`](#insn-00bcef10) → [`00bcef14`](#insn-00bcef14)
- ブロック [`00bcef14`](#insn-00bcef14) 範囲 `[['00bcef14', '00bcef2b']]`
  - `CONDITIONAL_JUMP` [`00bcef28`](#insn-00bcef28) → [`00bcef44`](#insn-00bcef44)
  - `FALL_THROUGH` [`00bcef28`](#insn-00bcef28) → [`00bcef2c`](#insn-00bcef2c)
- ブロック [`00bcef2c`](#insn-00bcef2c) 範囲 `[['00bcef2c', '00bcef43']]`
  - `FALL_THROUGH` [`00bcef40`](#insn-00bcef40) → [`00bcef44`](#insn-00bcef44)
- ブロック [`00bcef44`](#insn-00bcef44) 範囲 `[['00bcef44', '00bcef6b']]`
  - `CONDITIONAL_JUMP` [`00bcef68`](#insn-00bcef68) → [`00bcef8c`](#insn-00bcef8c)
  - `FALL_THROUGH` [`00bcef68`](#insn-00bcef68) → [`00bcef6c`](#insn-00bcef6c)
- ブロック [`00bcef6c`](#insn-00bcef6c) 範囲 `[['00bcef6c', '00bcef7b']]`
  - `FALL_THROUGH` [`00bcef78`](#insn-00bcef78) → [`00bcef7c`](#insn-00bcef7c)
- ブロック [`00bcef7c`](#insn-00bcef7c) 範囲 `[['00bcef7c', '00bcef83']]`
  - `FALL_THROUGH` [`00bcef80`](#insn-00bcef80) → [`00bcef84`](#insn-00bcef84)
- ブロック [`00bcef84`](#insn-00bcef84) 範囲 `[['00bcef84', '00bcef8b']]`
- ブロック [`00bcef8c`](#insn-00bcef8c) 範囲 `[['00bcef8c', '00bcef9b']]`

## 命令位置別の参照

- [`00bceefc`](#insn-00bceefc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef00`](#insn-00bcef00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef04`](#insn-00bcef04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef10`](#insn-00bcef10) → [`00bcef8c`](#insn-00bcef8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef20`](#insn-00bcef20) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bcef28`](#insn-00bcef28) → [`00bcef44`](#insn-00bcef44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef4c`](#insn-00bcef4c) → `01126350`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcef5c`](#insn-00bcef5c) → [`00574cac`](../00574/00574cac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574cac` · 推定シンボル `None` · 推定型 `None`
- [`00bcef64`](#insn-00bcef64) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcef68`](#insn-00bcef68) → [`00bcef8c`](#insn-00bcef8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef74`](#insn-00bcef74) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef78`](#insn-00bcef78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef8c`](#insn-00bcef8c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcef90`](#insn-00bcef90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bceefc`](#insn-00bceefc)

~~~json
{
  "source": "00bceefc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef00`](#insn-00bcef00)

~~~json
{
  "source": "00bcef00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef04`](#insn-00bcef04)

~~~json
{
  "source": "00bcef04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef10`](#insn-00bcef10)

~~~json
{
  "source": "00bcef10",
  "target": "00bcef8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef20`](#insn-00bcef20)

~~~json
{
  "source": "00bcef20",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcef28`](#insn-00bcef28)

~~~json
{
  "source": "00bcef28",
  "target": "00bcef44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef4c`](#insn-00bcef4c)

~~~json
{
  "source": "00bcef4c",
  "target": "01126350",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126350",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcef5c`](#insn-00bcef5c)

~~~json
{
  "source": "00bcef5c",
  "target": "00574cac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcef64`](#insn-00bcef64)

~~~json
{
  "source": "00bcef64",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcef68`](#insn-00bcef68)

~~~json
{
  "source": "00bcef68",
  "target": "00bcef8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef74`](#insn-00bcef74)

~~~json
{
  "source": "00bcef74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef78`](#insn-00bcef78)

~~~json
{
  "source": "00bcef78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef8c`](#insn-00bcef8c)

~~~json
{
  "source": "00bcef8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcef90`](#insn-00bcef90)

~~~json
{
  "source": "00bcef90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
