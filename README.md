# PU-wifi
A python program written by [@saicharankandukuri](https://github.com/SaicharanKandukuri/puwifi) to keep you device connected to parul university wifi
![LookingAroundGIF](https://user-images.githubusercontent.com/68287637/146674077-b5b823be-8146-4770-a2e7-7ced5a04843c.gif)

![image](https://user-images.githubusercontent.com/68287637/146674599-1568723d-6c70-49e8-8d71-1275ab3b169d.png)


[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSaicharanKandukuri%2Fpuwifi.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FSaicharanKandukuri%2Fpuwifi?ref=badge_shield)
[![CodeQL](https://github.com/SaicharanKandukuri/puwifi/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/SaicharanKandukuri/puwifi/actions/workflows/codeql-analysis.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/saicharankandukuri/puwifi/badge)](https://www.codefactor.io/repository/github/saicharankandukuri/puwifi)

# Installation
- make sure you installed python in your OS
```bash
git clone https://github.com/SaicharanKandukuri/puwifi
cd puwifi
pip install -r requirements.txt
```
# Usage

### General
#### 🪵 One-time login `-l`
you can login with `-l` or `--login` argument
```cmd
python3 puwifi.py -l -u YOUR_USERNAME -p YOUR_PASSWORD
```
#### 💥 Logout from puwifi
for logout use option `-o` or `--logout` argument
```cmd
python3 puwifi.py -o -u YOUR_PASSWORD -p YOUR_PASSWORD 
```
<!--
> idk why logout requires username and password too! ( vunerability ? )
--> 

#### ♾️ Forever login mode `-k`
this is what the aim of repo

`-k` or `--keep-alive` attribute is say script to run a forever loop!
> scripts tries to contact `google.com` if connection fails script tries to send login request to host *i.e: 10.0.0.1* with username & password provied with `-u` & `-p` arguments
```cmd
python3 puwifi.py -k -u YOUR_PASSWORD -p YOUR_PASSWORD 
```

![PusheenCatGIF](https://user-images.githubusercontent.com/68287637/146673862-cdb4f86e-c55b-470e-aa3f-b98dd362c6fb.gif)
###### go watch your videos now
<hr>

# Finally
This repo is made fully on self-intrest cause iam a student in parul university, wifi here is `great&fast` but a bit tricky
![RepeatJumpGIF](https://user-images.githubusercontent.com/68287637/146674165-5d586b3c-dfce-41d7-8ebe-54917b27fb91.gif)

so instead of playing dino i made this script by re-enginerring an year old puwifi login website & used some of knowledge to make this script happen


🐣 follow me on in [github](https://github.com/SaicharanKandukuri), [Twitter](https://twitter.com/AtonZman1x1)

🎮 Add me on discord: SaicharanKandukuri#3741

🌟 If this work of me helped you make sure you start this repo, or buy me a juice of coffee when we meet 🥤


> ⚠️ DOnt use practices used in this code for any kind of mischievous things. i need wifi working

# Licence
[GPL-3.0 License](https://github.com/SaicharanKandukuri/puwifi/blob/main/LICENSE) Copyright ©️ saicharankandukuri 

<details>

  <summary> Third-party Licences </summary>
---

# 3rd-Party Software for [puwifi]()



The following 3rd-party software packages may be used by or distributed with **puwifi**.  Any information relevant to third-party vendors listed below are collected using common, reasonable means.


Date generated | Revision ID
:------------: | :----------:
12/01/21 | e9a24a7e5a62b8e9e16ec2dbcc6d3d23aabded34

---

## Dependencies

### [requests (2.26.0)](https://requests.readthedocs.io)

#### Declared Licenses

Apache-2.0

```

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

```

#### Other Licenses

MIT

```
Copyright (c) 2021, requests Contributors
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

### [rich (10.15.1)](https://github.com/willmcgugan/rich)

#### Declared Licenses

MIT

```
Copyright (c) 2020 Will McGugan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

#### Other Licenses

---

[fossa]: # "Do not touch the comments below"
[fossa]: # "==depsig=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855=="

</details>

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSaicharanKandukuri%2Fpuwifi.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FSaicharanKandukuri%2Fpuwifi?ref=badge_large)

